from Persona import Persona
from datetime import datetime, timedelta

class Chofer(Persona):
    _choferes = []

    def __init__(self, nombre: str = "", edad: int = 0, id: int = 0, sueldo: int = 0,
                 cantidadHorasConducidas: int = 0, empresa: "Empresa" = None,
                 puntajeEficienciaTiempos: int = 0, puntajeConsumoCombustible: int = 0,
                 puntajeDefinitivo: float = 0, bus: "Bus" = None, horario: list[tuple[datetime]] = []):
        super().__init__(nombre, edad, id)
        self.setEmpresa(empresa)
        self._sueldo = sueldo
        self.setBus(bus)
        self._cantidadHorasConducidas = cantidadHorasConducidas
        self._puntajeEficienciaTiempos = puntajeEficienciaTiempos
        self._puntajeConsumoCombustible = puntajeConsumoCombustible
        self._puntajeDefinitivo = puntajeDefinitivo
        self.setHorario(horario)
        Chofer._choferes.append(self)

    # Definiendo Getters y Setters
    def getSueldo(self) -> int:
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

    def getEmpresa(self) -> "Empresa":
        return self._empresa
    
    def setEmpresa(self, empresa: "Empresa"):
        from Empresa import Empresa

        if empresa is None:
            self._empresa = None
        if isinstance(empresa, Empresa):
            self._empresa = empresa

    def getBus(self) -> "Bus":
        return self._bus

    def setBus(self, bus: "Bus"):
        from Bus import Bus

        if bus is None:
            self._bus = None
        if isinstance(bus, Bus):
            self._bus = bus

    def getHorario(self) -> list[tuple[datetime]]:
        return self._horario

    def setHorario(self, horario: list[tuple[datetime]]):
        self._horario = []
        for lapso in horario:
            if isinstance(lapso, tuple):
                self.anadirRuta(lapso[0], lapso[1])

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

    def mostrarDatos(self) -> str:
        return f"Soy el Chofer {self.getNombre()} tengo {self.getEdad()} años y mi ID es {self.getId()}"

    def isDisponible(self, fechaInicio: datetime, fechaFinal: datetime) -> bool:
        """
        Determina si el rango [fecha inicial, fecha final] se cruza con los horarios
        de los lapsos en que el chofer estpa comprometido.

        Parámetros:
            - fechaInicial: datetime,
                Comienzo del rango horario
            - fechaFinal: datetime,
                Conclusión del rango horario

            Retorna:
                - disponibilidad: bool,
                    Valor que especifica si el chofer está disponible en ese rango horario.
        """

        # Verificación de errores.
        if fechaInicio > fechaFinal:
            return False

        # Se busca alguna colisión con el horario.
        for lapso in self._horario:
            if (lapso[0] < fechaFinal + timedelta(hours = 1)) and (lapso[1] > fechaInicio - timedelta(hours = 1)):
                return False

        # Devolviendo que está disponible en caso de no haber colisión
        return True

    def anadirRuta(self, nuevoLapso: tuple[datetime]) -> tuple[datetime]:
        """
        Busca si se puede agregar el lapso en las ya establecidas para el chofer,
        mostrando una advertencia si no puede ser añadido.

        Parámetros:
            - nuevoLapso: tuple[datetime],
                (Fecha inicio, Fecha fin) a ser agregado.

        Retorna:
            - lapsoNoAsignado.
                Devuelve el nuevoLapso si este no puede ser asignado.
        """

        # Verificación de errores.
        if len(nuevoLapso) != 2:
            return nuevoLapso

        # Se busca dónde devería ir el nuevo lapso.
        posicion = 0
        for lapso in self._horario:
            # Se mira si el nuevo laspo está a la derecha de los
            # ya existentes.
            if lapso[0] < nuevoLapso[0]:
                # Se encuentra en un margen aceptable.
                if lapso[1] < nuevoLapso[0] - timedelta(hours = 1):
                    posicion += 1
                else:
                    posicion = -1
                    break
            # Ahora se mira  si se encuentra a la izquierda.
            else:
                # No dejan el margen aceptable.
                if nuevoLapso[1] > lapso[0] - timedelta(hours = 1):
                    posicion = -1
                    break

        # Si no se interseca con ningún lapso, se añade correctamente.
        if posicion != -1:
            self._horario.insert(posicion, nuevoLapso)
            return None
        else:
            return nuevoLapso

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
