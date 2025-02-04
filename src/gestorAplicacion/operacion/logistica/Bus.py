from datetime import datetime
import random as rand
from gestorAplicacion.administracion.Ruta import Ruta
from gestorAplicacion.administracion.Empresa import Empresa
from gestorAplicacion.operacion.individuos.Pasajero import Pasajero
from gestorAplicacion.operacion.logistica.Asiento import Asiento


class Bus:
    # Esto nos dira la cantidad maxima de equipaje que soporta cada bus ¡¡Peso en Kg!!
    _PESO_MAXIMO = {"LIGERO": 500, "MEDIO": 750, "PESADO": 1000, "EXTRA_PESADO": 1250}
    _COSTO_REPARACIONES = {
        "RUEDA_PINCHADA": 100000,
        "SOPORTE_MOTOR": 1500000,
        "SOPORTE_TIPO_COMBUSTIBLE": 50000,
        "LLANTA_DANADA": 100000,
        "RETROVISOR_DANADO": 50000,
        "TAPA_LLANTA_DANADA": 50000,
    }
    _buses = []

    # Este es el constructor de la clase, donde inicializamos los atributos
    def __init__(
        self,
        placa: str = "",
        cantidadAsientos: int = 20,
        asientos: list = [],
        kilometrosRecorridos: float = 0.0,
        rutasFuturas: list = [],
        empresa: Empresa = None,
        equipaje: list = [],
        consumo: float = 0.0,
        pesoMaximo: float = 0.0,
        estado: str = "Perfecto Estado",
    ):
        self.placa = placa
        self._cantidadAsientos = cantidadAsientos
        self._asientos = asientos
        self._kilometrosRecorridos = kilometrosRecorridos
        self._rutasFuturas = rutasFuturas
        self.empresa = empresa
        self._equipaje = equipaje
        self._consumo = consumo
        self._pesoMaximo = pesoMaximo
        self._estado = estado
        # Agregamos el bus a la lista de buses
        if self.empresa is not None:
            self.empresa.agregarBus(self)

    def getCantidadAsientos(self):
        return self._cantidadAsientos

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, value: list):
        self._asientos = value

    def getKilometrosRecorridos(self):
        return self._kilometrosRecorridos

    def setKilometrosRecorridos(self, value: float):
        self._kilometrosRecorridos = value

    def getRutasFuturas(self):
        return self._rutasFuturas

    def setRutasFuturas(self, value: list):
        self._rutasFuturas = value

    def getEquipaje(self):
        return self._equipaje

    def setEquipaje(self, value: list):
        self._equipaje = value

    def getConsumo(self):
        return self._consumo

    def setConsumo(self, value: float):
        self._consumo = value

    def getPesoMaximo(self):
        return self._pesoMaximo

    def setPesoMaximo(self, value: float):
        self._pesoMaximo = value

    # Métodos de Clase
    @classmethod
    def anadirBus(cls, bus: "Bus"):
        cls._buses.append(bus)

    def cantidadBuses(cls) -> int:
        return len(cls._buses)

    def getBuses(cls):
        return cls._buses

    # Métodos de Instancia
    def isDisponbile(self, fechaInicio: datetime, fechaLlegada: datetime) -> str:
        # Determina si el bus está disponible para el rango de fechas especificado.
        # Determina si el rango [fecha inicial, fecha final] se cruza con los horarios
        # de las rutas que el bus debe cumplir.
        #
        # Parámetros:
        # - fechaInicial: LocalDateTime,
        # Comienzo del rango horario
        # - fechaFinal: LocalDateTime,
        # Conclusión del rango horario
        #
        # Retorna:
        # - disponibilidad: Boolean,
        # Valor que especifica si el bus está disponible en ese rango horario.
        #

        for ruta in self._rutasFuturas:

            if not (
                fechaLlegada < ruta.getFechaSalida()
                or fechaInicio > ruta.getFechaLlegada()
            ):
                return "El bus no está disponible en esa fecha."
        return "El bus está disponible en esa fecha."

    def anadirRutaFutura(self, rutaNueva: Ruta) -> str:
        # Agrega una nueva ruta al bus.
        #
        # Parámetros:
        # - ruta: Ruta,
        # La ruta que se quiere agregar al bus.
        #
        # Retorna:
        # - resultado: Boolean,
        # Indica si la ruta se agregó correctamente.
        #
        if rutaNueva in self._rutasFuturas:
            return "Está ruta ya se encuentra en los futuros viajes."
        for ruta in self._rutasFuturas:
            if not (
                rutaNueva.getFechaLlegada() + datetime.timedelta(hours=1)
                < ruta.getFechaSalida()
                or rutaNueva.getFechaSalida() - datetime.timedelta(hours=1)
                > ruta.getFechaLlegada()
            ):
                return "No se puede añadir está ruta por su fecha de salida o llegada."
        return "Está ruta ha sido añadida exitosamente."

    def quitarRutaFutura(self, ruta: "Ruta") -> str:
        """Remueve la ruta especificada en caso de estar presente en una ruta del bus.
                 *
        Parámetros:
        - ruta: Ruta,
        Ruta a ser añadida.
        """
        if ruta in self._rutasFuturas:
            self._rutasFuturas.remove(ruta)
            ruta.setBusAsociado(None)
            return "Se ha quitado la ruta con exito."
        return "Esta ruta no se encuentra en los futuros viajes."

    def asignarPasajero(self, pasajero: "Pasajero") -> str:
        if len(self.getAsientos()) < self._cantidadAsientos:
            asiento = Asiento(
                self,
                False,
                pasajero,
            )
            self.getAsientos().append(asiento)
            return f"Pasajero {pasajero.getNombre()} se ha asignado correctamente en el Bus {self.placa}."
        return f"Pasajero {pasajero.getNombre()} no fue asignado correctamente por falta de asientos en el bus {self.placa}"

    def eliminarPasajero(self, pasajero: "Pasajero") -> str:
        # Remueve un pasajero del bus.
        #
        # Retorna:
        # - resultado: String,
        # Indica si el pasajero se ha removido correctamente.
        asientos = self.getAsientos()
        for asiento in asientos:
            if asiento.getPasajero() == pasajero:
                asientos.remove(asiento)
                return f"Pasajero {pasajero.getNombre()} se ha eliminado correctamente del bus {self.placa}."
        return f"El pasajero {pasajero.getNombre()} no se encuentra en el bus {self.placa}."

    def reparar(self):
        def confirmar(self):
            return input("¿Confirma la reparación? (s/n): ")

        for estado in Bus._COSTO_REPARACIONES:
            if self._estado == self._estado:
                return f"El bus necesita reparar su {estado}. El costo de reparación es {Bus._COSTO_REPARACIONES[estado]}."
            if confirmar(self) == "s":
                self._estado = self._estado
                return f"La reparación ha sido confirmada y el bus se ha restablecido a su estado original."
            return "La reparación ha sido cancelada."

    def verificarIntegridad(self):
        if (self._estado == "") or (self._estado == "Perfecto Estado"):
            return "El bus se encuentra en un estado perfecto."
        return "El bus se encuentra en un {self._estado}"

    def calcularConsumoCombustible(self):
        # Calcula el consumo de combustible del bus en base a los kilometros recorridos y el consumo promedio del bus.
        #
        # Retorna:
        # - consumoCombustible: float,
        # Consumo de combustible en litros recorridos.
        return self._kilometrosRecorridos * self._consumo

    def danoAleatorio(self) -> str:
        return rand.choice(Bus._COSTO_REPARACIONES)
