from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre: str = "", edad: int = 0, id: int = 0):
        self._nombre = nombre
        self._edad = edad
        self._id = id

    @abstractmethod
    def mostrarDatos(self) -> str:
            pass

    # Defieniendo getters y setters
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad: int):
        self._edad = edad

    def getId(self):
        return self._id

    def setId(self, id: int):
        self._id = id
