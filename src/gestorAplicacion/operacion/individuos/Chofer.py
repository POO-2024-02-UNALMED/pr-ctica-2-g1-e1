from Persona import Persona


class Chofer(Persona):
    _choferes = []

    def __init__(
        self,
        nombre: str = "",
        edad: int = 0,
        id: int = 0,
        sueldo: int = 0,
        cantidadHorasConducidas: int = 0,
        empresa: object = None,
        puntajeEficienciaTiempos: int = 0,
        puntajeConsumoCombustible: int = 0,
        puntajeDefinitivo: float = 0,
        bus: object = None,
        horario: list = [],
    ):
        super().__init__(nombre, edad, id)
        self._empresa = empresa
        self._sueldo = sueldo
        self._bus = bus
        self._cantidadHorasConducidas = cantidadHorasConducidas
        self._puntajeEficienciaTiempos = puntajeEficienciaTiempos
        self._puntajeConsumoCombustible = puntajeConsumoCombustible
        self._puntajeDefinitivo = puntajeDefinitivo
        self._horario = horario
        Chofer._choferes.append(self)

    # Definiendo Getters y Setters
    def getSueldor(self) -> int:
        return self._sueldo

    def getCantidadHorasConducidas(self) -> int:
        return self._cantidadHorasConducidas

    def getPuntajeEficienciaTiempos(self) -> int:
        return self._puntajeEficienciaTiempos

    def getPuntajeConsumoCombustible(self) -> int:
        return self._puntajeConsumoCombustible

    def getPuntajeDefinitivo(self) -> float:
        return self._puntajeDefinitivo

    def getHorario(self) -> list:
        return self._horario

    def setSueldo(self, sueldo: int):
        self._sueldo = sueldo

    def setCantidadHorasConducidas(self, cantidadHorasConducidas: int):
        self._cantidadHorasConducidas = cantidadHorasConducidas

    def setPuntajeEficienciaTiempos(self, puntajeEficienciaTiempos: int):
        self._puntajeEficienciaTiempos = puntajeEficienciaTiempos

    def setPuntajeConsumoCombustible(self, puntajeConsumoCombustible: int):
        self._puntajeConsumoCombustible = puntajeConsumoCombustible

    def setPuntajeDefinitivo(self, puntajeDefinitivo: float):
        self._puntajeDefinitivo = puntajeDefinitivo

    # Metodos de Clase
    @classmethod
    def getChoferes(cls) -> list:
        return cls._choferes

    @classmethod
    def getCantidadChoferes(cls) -> int:
        return len(cls._choferes)

    # Métodos de Instacia
    def aumentarSueldo(self, aumento):
        self._sueldo += aumento

    def mostrarDatos(self):
        print(
            f"Soy el Chofer {self.getNombre()} tengo {self.getEdad()} años y mi ID es {self.getId()}"
        )

    def isDisponible(self) -> bool:
        pass

    def calcularEficienciaTiempos(self):
        pass

    def calcularConsumoCombustible(self):
        pass

    def calcularPuntajeDefinitivo(self):
        pass

    def generarInformeRendimiento(self):
        pass

    def calcularSalario(self):
        pass

    def registrarTurno(self):
        pass

    def registrarViaje(self):
        pass
