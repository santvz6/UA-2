class Paquete:
    def __init__(self, direccion:str, zona: int, peso: int):
        self.__direccion = direccion
        self.__zona = zona
        self.__peso = peso

    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def zona(self):
        return self.__zona
    
    @property
    def peso(self):
        return self.__peso