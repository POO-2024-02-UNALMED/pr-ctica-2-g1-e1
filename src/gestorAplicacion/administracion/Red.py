from abc import ABC, abstractmethod

class Red(ABC):
    paradas = ["BOGOTA", "MEDELLIN", "BARRANQUILLA", "CALI", "PEREIRA", "TUNJA",
               "VILLAVICENCIO", "CARTAGENA", "IBAGUE", "PASTO"]

    def Parada(i: int):
        # Devuelve la parada en la posición i-ésima.
        return Red.paradas[i]