from Red import Red
from datetime import datetime
from gestorAplicacion.operacion.individuos.Chofer import Chofer


class Ruta(Red):
    _rutas = []
    _DIFICULTAD_BAJA = 50  # Km
    _DIFICULTAD_MEDIA = 150  # Km
    _DIFICULTAD_ALTA = 300  # Km
    _DIFICULTAD_MUY_ALTA = 500  # Km

    def __init__(
        self,
        idRuta: int,
        busAsociado: object = None,
        choferAsociado: Chofer = None,
        fechaSalida: datetime = None,
        fechaLlegada: datetime = None,
        lugarInicio: str = "",
        lugarFin: str = "",
        distancia: float = 0.0,
        tiempoEstimado: float = 0.0,
        estado: bool = False,
    ):
        self._idRuta = idRuta
        self._busAsociado = busAsociado
        self._choferAsociado = choferAsociado
        self._fechaSalida = fechaSalida
        self._fechaLlegada = fechaLlegada
        self._lugarInicio = lugarInicio
        self._lugarFin = lugarFin
        self._distancia = distancia
        self._tiempoEstimado = tiempoEstimado
        self._estado = estado

    # Definir Getters y Setters
    def getIdRuta(self) -> int:
        return self._idRuta

    def getBusAsociado(self) -> object:
        return self._busAsociado

    def getChoferAsociado(self) -> Chofer:
        return self._choferAsociado

    def getFechaSalida(self) -> datetime:
        return self._fechaSalida

    def getFechaLlegada(self) -> datetime:
        return self._fechaLlegada

    def getLugarInicio(self) -> str:
        return self._lugarInicio

    def getLugarFin(self) -> str:
        return self._lugarFin

    def getDistancia(self) -> float:
        return self._distancia

    def getTiempoEstimado(self) -> float:
        return self._tiempoEstimado

    def getEstado(self) -> bool:
        return self._estado

    def setIdRuta(self, idRuta: int):
        self._idRuta = idRuta

    def setBusAsociado(self, busAsociado: object):
        self._busAsociado = busAsociado

    def setChoferAsociado(self, choferAsociado: Chofer):
        self._choferAsociado = choferAsociado

    def setFechaSalida(self, fechaSalida: datetime):
        self._fechaSalida = fechaSalida

    def setFechaLlegada(self, fechaLlegada: datetime):
        self._fechaLlegada = fechaLlegada

    def setLugarInicio(self, lugarInicio: str):
        self._lugarInicio = lugarInicio

    def setLugarFin(self, lugarFin: str):
        self._lugarFin = lugarFin

    def setDistancia(self, distancia: float):
        self._distancia = distancia

    def setTiempoEstimado(self, tiempoEstimado: float):
        self._tiempoEstimado = tiempoEstimado

    def setEstado(self, estado: bool):
        self._estado = estado

    # Métodos de Clase
    @classmethod
    def getRutas(cls) -> list:
        return cls._rutas

    @classmethod
    def setRutas(cls, rutas):
        cls._rutas = rutas

    @classmethod
    def anadirRutas(cls, ruta):
        cls._rutas.append(ruta)
    
    #Metodos de Instancia
