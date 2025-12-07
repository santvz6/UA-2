import cv2
import threading
import time
import requests
import psutil
import os
from datetime import datetime
from collections import defaultdict

class CameraManager:
    def __init__(self, source_urls, capture_interval=5, vm_endpoint=None, cloud_endpoint=None):
        self.source_urls = source_urls
        self.capture_interval = capture_interval  # segundos entre capturas
        self.vm_endpoint = vm_endpoint
        self.cloud_endpoint = cloud_endpoint
        self.captures = {}
        self.threads = []
        self.stats = defaultdict(list)
        self.running = False
        os.makedirs("frames", exist_ok=True)

    def _init_cameras(self):
        for url in self.source_urls:
            cap = cv2.VideoCapture(url)
            if not cap.isOpened():
                print(f"[WARN] No se pudo abrir el stream: {url}")
            else:
                self.captures[url] = cap

    def _release_cameras(self):
        for cap in self.captures.values():
            cap.release()
        cv2.destroyAllWindows()

    def _send_frame(self, frame, endpoint):
        _, img_encoded = cv2.imencode('.jpg', frame)
        files = {'frame': img_encoded.tobytes()}
        start = time.time()
        try:
            resp = requests.post(endpoint, files=files, timeout=2)
            latency = time.time() - start
            return resp, latency, len(img_encoded)
        except Exception as e:
            print(f"[ERROR] Error al enviar frame: {e}")
            return None, 0, 0

    def _monitor_resources(self):
        proc = psutil.Process(os.getpid())
        cpu = proc.cpu_percent(interval=0.1)
        mem = proc.memory_info().rss / (1024 * 1024)  # MB
        net = psutil.net_io_counters()
        return cpu, mem, net.bytes_sent, net.bytes_recv

    def _camera_loop(self, url):
        cap = self.captures[url]
        while self.running:
            t0 = time.time()
            ret, frame = cap.read()
            if not ret:
                print(f"[WARN] No se pudo leer un frame de: {url}")
                time.sleep(self.capture_interval)
                continue

            # Guardar frame localmente
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"frames/frame_{timestamp}_{hash(url) % 10000}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[INFO] Guardado: {filename}")

            # Enviar a la VM
            if self.vm_endpoint:
                resp_vm, lat_vm, size_vm = self._send_frame(frame, self.vm_endpoint)
                cpu, mem, sent, recv = self._monitor_resources()
                self.stats['vm_latency'].append(lat_vm)
                self.stats['vm_cpu'].append(cpu)
                self.stats['vm_mem'].append(mem)
                self.stats['vm_bandwidth_sent'].append(sent)

            # Enviar a la nube (si existiera)
            if self.cloud_endpoint:
                resp_cl, lat_cl, size_cl = self._send_frame(frame, self.cloud_endpoint)
                cpu, mem, sent, recv = self._monitor_resources()
                self.stats['cloud_latency'].append(lat_cl)
                self.stats['cloud_cpu'].append(cpu)
                self.stats['cloud_mem'].append(mem)
                self.stats['cloud_bandwidth_sent'].append(sent)

            # Esperar hasta el siguiente frame
            dt = time.time() - t0
            if dt < self.capture_interval:
                time.sleep(self.capture_interval - dt)

    def start(self):
        self._init_cameras()
        self.running = True
        for url in self.captures:
            th = threading.Thread(target=self._camera_loop, args=(url,), daemon=True)
            th.start()
            self.threads.append(th)
        print("[INFO] CameraManager iniciado.")

    def stop(self):
        self.running = False
        for th in self.threads:
            th.join()
        self._release_cameras()
        print("[INFO] CameraManager detenido.")

    def report(self):
        report = {}
        for k, v in self.stats.items():
            if v:
                report[k] = {
                    'min': min(v),
                    'max': max(v),
                    'avg': sum(v) / len(v)
                }
        return report


if __name__ == '__main__':

    cam_urls = [
        # Aquí deberían ir las cámaras consecutivas
    ]

    vm_url = 'http://<VM_IP>:5000/analyze' 
    cloud_url = None  # Si no hay app Cloud en Azure, puede quedar como None

    manager = CameraManager(cam_urls, capture_interval=5, vm_endpoint=vm_url, cloud_endpoint=cloud_url)

    try:
        manager.start()
        time.sleep(60)  # Ejecutar por 1 minuto
    finally:
        manager.stop()
        stats = manager.report()
        print("Reporte de rendimiento:")
        for k, v in stats.items():
            print(f"{k}: min={v['min']:.2f}, avg={v['avg']:.2f}, max={v['max']:.2f}")
