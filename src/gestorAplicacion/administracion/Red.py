from abc import ABC, abstractmethod


class Red(ABC):
    destinos = {
        "BOGOTA": "BOGOTA",
        "MEDELLIN": "MEDELLIN",
        "BARRANQUILLA": "BARRANQUILLA",
        "CALI": "CALI",
        "PEREIRA": "PEREIRA",
        "TUNJA": "TUNJA",
        "VILLAVICENCIO": "VILLAVICENCIO",
        "CARTAGENA": "CARTAGENA",
        "IBAGUE": "IBAGUE",
        "PASTO": "PASTO",
    }

    def __init__(self):
        pass
