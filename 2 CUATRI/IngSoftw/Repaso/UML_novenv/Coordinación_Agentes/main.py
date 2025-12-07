from tarea import Tarea
from coordinador import Coordinador

import logging


logging.basicConfig(
    level=logging.INFO,
    filemode="a",
    filename="logs/agentes.log")

if __name__ == "__main__":

    tareas = [
        Tarea("Instalación de router", "ASISTENCIA", "PENDIENTE"),
        Tarea("Seguimiento a cliente potencial", "COMERCIAL", "PENDIENTE"),
        Tarea("Revisión de red local", "ASISTENCIA", "PENDIENTE"),
        Tarea("Presentación de propuesta comercial", "COMERCIAL", "PENDIENTE"),
        Tarea("Soporte técnico remoto", "ASISTENCIA", "PENDIENTE"),
        Tarea("Llamada de cierre de venta", "COMERCIAL", "PENDIENTE"),
        Tarea("Configuración de impresora", "ASISTENCIA", "PENDIENTE"),
        Tarea("Envío de cotización", "COMERCIAL", "PENDIENTE"),
        Tarea("Asistencia en sitio", "ASISTENCIA", "PENDIENTE"),
        Tarea("Visita a cliente corporativo", "COMERCIAL", "PENDIENTE"),
    ]

    cord = Coordinador()

    for t in tareas:
        print(f"{t.descripcion} - {t.estado}")
        cord.asignar_tarea(t)
        print(f"{t.descripcion} - {t.estado}")

