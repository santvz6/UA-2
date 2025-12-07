class Tarea:
    def __init__(self, descripcion: str, tipo:str, estado: str):
        self.descripcion = descripcion

        if tipo not in ["ASISTENCIA", "COMERCIAL"] or \
            estado not in ["PENDIENTE", "COMPLETADA"]:
            raise ValueError
        
        self.tipo = tipo
        self.estado = estado