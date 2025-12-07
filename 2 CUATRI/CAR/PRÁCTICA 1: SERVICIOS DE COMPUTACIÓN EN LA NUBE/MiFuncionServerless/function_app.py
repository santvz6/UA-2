import azure.functions as func
import json
import logging
import time

app = func.FunctionApp()

@app.route(route="procesar_frame")
def procesar_frame(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Procesando frame recibido.')
    
    start_time = time.time()  

    try:
        req_body = req.get_json()
        frame_data = req_body.get('frame')
        if not frame_data:
            return func.HttpResponse("No se ha recibido ningún frame en la petición.", status_code=400)
        
        # NOTE
        # Aquí iría el procesamiento real del frame, por ejemplo detección.
        # Para simular, calculamos una "eficiencia" ficticia.
        longitud_frame = len(frame_data)
        eficiencia = 0.95

        elapsed_time = time.time() - start_time
        
        # Resultado con métricas
        resultado = {
            "mensaje": "Frame procesado correctamente",
            "detalles": {
                "longitud_frame": longitud_frame,
                "eficiencia_deteccion": eficiencia,
                "tiempo_respuesta_segundos": round(elapsed_time, 4)
            }
        }

        logging.info(f"Procesado frame: eficiencia={eficiencia}, tiempo={elapsed_time:.4f}s")
        
        return func.HttpResponse(json.dumps(resultado), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error procesando frame: {e}")
        return func.HttpResponse("Error procesando la petición.", status_code=500)
