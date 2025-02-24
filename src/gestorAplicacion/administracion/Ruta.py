from Red import Red
from datetime import datetime

class Ruta(Red):
    _rutas = []
    _DIFICULTAD_BAJA = 50  # Km
    _DIFICULTAD_MEDIA = 150  # Km
    _DIFICULTAD_ALTA = 300  # Km
    _DIFICULTAD_MUY_ALTA = 500  # Km

    def __init__(self, busAsociado: "Bus" = None, choferAsociado: "Chofer" = None,
                 fechaSalida: datetime = datetime.now(), fechaLlegada: datetime = datetime.now(),
                 lugarInicio: str = "", lugarFin: str = "", distancia: float = 0.0,
                 tiempoEstimado: float = 0.0):
        self._idRuta = len(Ruta._rutas)
        self.setBusAsociado(busAsociado)
        self.setChoferAsociado(choferAsociado)
        self._fechaSalida = fechaSalida
        self._fechaLlegada = fechaLlegada
        self._lugarInicio = lugarInicio
        self._lugarFin = lugarFin
        self._distancia = distancia
        if (fechaLlegada is not None) and (fechaSalida is not None):
            self._tiempoEstimado = (fechaLlegada - fechaSalida).total_seconds() / 3600 # Horas
        else:
            self._tiempoEstimado = None

        # Agregando la ruta a las lista de rutas.
        Ruta.anadirRuta(self)

    # Definir Getters y Setters
    def getIdRuta(self) -> int:
        return self._idRuta

    def getBusAsociado(self) -> "Bus":
        return self._busAsociado

    def getChoferAsociado(self) -> "Chofer":
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

    def setIdRuta(self, idRuta: int):
        self._idRuta = idRuta

    def setBusAsociado(self, busAsociado: "Bus"):
        from Bus import Bus

        if isinstance(busAsociado, Bus):
            self._busAsociado = busAsociado
        try:
            self._busAsociado
        except AttributeError:
            self._busAsociado = None

    def setChoferAsociado(self, choferAsociado: "Chofer"):
        from Chofer import Chofer

        if isinstance(choferAsociado, Chofer):
            self._choferAsociado = choferAsociado
        try:
            self._choferAsociado
        except AttributeError:
            self._choferAsociado = None

    def setFechaSalida(self, fechaSalida: datetime):
        try:
            if fechaSalida is not None:
                self._fechaSalida = fechaSalida
            if (self._fechaLlegada is not None) and (fechaSalida is not None):
                self._tiempoEstimado = (self._fechaLlegada - fechaSalida).total_seconds() / 3600 # Horas
            else:
                self._tiempoEstimado = None
        except AttributeError:
            if fechaSalida is not None:
                self._fechaSalida = fechaSalida

    def setFechaLlegada(self, fechaLlegada: datetime):
        try:
            if fechaLlegada is not None:
                self._fechaLlegada = fechaLlegada
            if (fechaLlegada is not None) and (self._fechaSalida is not None):
                self._tiempoEstimado = (fechaLlegada - self._fechaSalida).total_seconds() / 3600 # Horas
            else:
                self._tiempoEstimado = None
        except AttributeError:
            if fechaLlegada is not None:
                self._fechaLlegada = fechaLlegada

    def setLugarInicio(self, lugarInicio: str):
        self._lugarInicio = lugarInicio

    def setLugarFin(self, lugarFin: str):
        self._lugarFin = lugarFin

    def setDistancia(self, distancia: float):
        self._distancia = distancia

    def setTiempoEstimado(self, tiempoEstimado: float):
        self._tiempoEstimado = tiempoEstimado

    # Métodos de Clase
    @classmethod
    def getRutas(cls) -> list:
        return cls._rutas

    @classmethod
    def setRutas(cls, rutas: list):
        cls._rutas = []
        for ruta in rutas:
            cls.anadirRuta(ruta)

    @classmethod
    def anadirRuta(cls, ruta):
        if isinstance(ruta, Ruta):
            cls._rutas.append(ruta)
    
    #Metodos de Instancia