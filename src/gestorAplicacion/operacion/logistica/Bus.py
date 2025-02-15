from gestorAplicacion.administracion.Ruta import Ruta
from gestorAplicacion.administracion.Empresa import Empresa
from ..individuos.Pasajero import Pasajero
from Asiento import Asiento
from Maleta import Maleta

from datetime import datetime, timedelta
import random as rand

class Bus:
    # Esto nos dira la cantidad maxima de equipaje que soporta cada bus ¡¡Peso en Kg!!
    _PESO_MAXIMO = [500, 750, 1000, 1250]
    _COSTO_REPARACIONES = [("RUEDA_PINCHADA", 100000), ("SOPORTE_MOTOR", 1500000),
                           ("SOPORTE_TIPO_COMBUSTIBLE", 50000), ("LLANTA_DANADA", 100000),
                           ("RETROVISOR_DANADO", 50000), ("TAPA_LLANTA_DANADA", 50000)]
    _buses = []

    # Este es el constructor de la clase, donde inicializamos los atributos
    def __init__(self, placa: str = "", cantidadAsientos: int = 20, asientos: list[Asiento] = [],
                 kilometrosRecorridos: float = 0.0, rutasFuturas: list[Ruta] = [],
                 empresa: Empresa = None, equipaje: list[Maleta] = [], consumo: float = 0.0,
                 pesoMaximo: float = 0.0, estado: str = "Perfecto Estado"):
        self.placa = placa
        self._cantidadAsientos = cantidadAsientos
        self.setAsientos(asientos)
        self._kilometrosRecorridos = kilometrosRecorridos
        self.setRutasFuturas(rutasFuturas)
        self.setEmpresa(empresa)
        self.setEquipaje(equipaje)
        self._consumo = consumo
        self.setPesoMaximo(pesoMaximo)
        self._estado = estado

        # Agregamos el bus a la lista de buses
        if self.empresa is not None:
            self._empresa.agregarBus(self)

    def getCantidadAsientos(self):
        return self._cantidadAsientos

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, asientos: list[Asiento]):
        self._asientos = []
        for asiento in asientos:
            if isinstance(asiento, Asiento) and asiento not in self._asientos:
                self._asientos.append(asiento)

    def getKilometrosRecorridos(self):
        return self._kilometrosRecorridos

    def setKilometrosRecorridos(self, value: float):
        self._kilometrosRecorridos = value

    def getRutasFuturas(self):
        return self._rutasFuturas

    def setRutasFuturas(self, rutas: list[Ruta]) -> list[Ruta]:
        self._rutasFuturas = []
        rutasNoAnadidas = []
        for ruta in rutas:
            if isinstance(ruta, Ruta):
                if not self.anadirRuta(ruta):
                    rutasNoAnadidas.append(ruta)

        # Devolviendo las rutas que no pudieron ser añadidas.
        return rutasNoAnadidas

    def getEquipaje(self):
        return self._equipaje

    def setEquipaje(self, maletas: list[Maleta]):
        self._equipaje = []
        for maleta in maletas:
            if isinstance(maleta, Maleta):
                self._equipaje.append(maleta)

    def getConsumo(self):
        return self._consumo

    def setConsumo(self, value: float):
        self._consumo = value

    def getPesoMaximo(self):
        return self._pesoMaximo

    def setPesoMaximo(self, pesoMaximo: float):
        if pesoMaximo in Bus.PesoMaximo:
            self._pesoMaximo = pesoMaximo

    def getEmpresa(self) -> Empresa:
        return self._empresa

    def setEmpresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            self._empresa = empresa

    # Métodos de Clase
    @classmethod
    def anadirBus(cls, bus: "Bus"):
        if isinstance(bus, Bus) and bus not in Bus._buses:
            Bus._buses.append(bus)

    def cantidadBuses(cls) -> int:
        return len(cls._buses)

    def getBuses(cls):
        return cls._buses

    # Métodos de Instancia
    def isDisponbile(self, fechaInicio: datetime, fechaFinal: datetime) -> bool:
        """
        Determina si el rango [fecha inicial, fecha final] se cruza con los horarios
        de las rutas que el bus debe cumplir.

        Parámetros:
            - fechaInicio: datetime,
                Comienzo del rango horario
            - fechaFinal: datetime,
                Conclusión del rango horario

        Retorna:
            - disponibilidad: bool,
                Valor que especifica si el bus está disponible en ese rango horario.
        """

        # Verificación de errores.
        if fechaInicio > fechaFinal:
            return False

        # Se busca si alguna de las rutas futuras
        # colisiona con el horario establecido.
        for ruta in self._rutasFuturas:
            if ((fechaInicio < ruta.getFechaLlegada() + timedelta(days = 1)) and
                (fechaFinal > ruta.getFechaSalida() - timedelta(days = 1))):
                return False

        # Si no colisiona con nada, devuelve que está disponible.
        return True

    def anadirRuta(self, nuevaRuta: Ruta) -> bool:
        """
        Busca si se puede agregar la ruta en las ya establecidas para el bus,
        mostrando una advertencia si la ruta no puede ser añadida.

        Parámetros:
            - nuevaRuta: Ruta,
                Ruta a ser añadida.
 
        Retorna:
            - asignado: bool,
                Indica si se pudo añadir la ruta.
        """

        # Verificación de errores.
        if not isinstance(nuevaRuta, Ruta): return False

        # Viendo si la ruta ya existe en la lista.
        if nuevaRuta in self._rutasFuturas:
            return False

        # Viendo si la nueva ruta tiene un horario compartido con una ya asignada. 
        for ruta in self._rutasFuturas:
            if not (nuevaRuta.getFechaLlegada() + datetime.timedelta(hours = 1) < ruta.getFechaSalida() or
                    nuevaRuta.getFechaSalida() - datetime.timedelta(hours = 1) > ruta.getFechaLlegada()):
                return False

        # Asignando el bus.
        nuevaRuta.setBusAsociado(self)
        self._rutasFuturas.append(nuevaRuta)
        return True

    def quitarRuta(self, ruta: Ruta):
        """
        Remueve la ruta especificada en caso de estar presente en una ruta del bus.

        Parámetros:
            - ruta: Ruta,
                Ruta a ser añadida.
        """

        # Quitando la ruta si hace parte de las asignadas.
        if ruta in self._rutasFuturas:
            self._rutasFuturas.remove(ruta)
            ruta.setBusAsociado(None)

    def hallarHueco(self, duracion: int) -> datetime:
        """
        Mira en el horario del bus a ver si encuentra un hueco de la duración especificada.

        Parámetros:
            - lapso: int,
                Tiempo que se necesita al bus.

        Retorna:
            - fecha: datetime,
                Fecha en la cual puede iniciar la actividad a reclutarlo.
        """

        # Viendo si tiene rutas.
        if self._rutasFuturas == []:
            return datetime.now() + timedelta(hours = 1)

        # Viendo si hay un hueco ahora. 
        if datetime.now() < self._rutasFuturas[0].getFechaSalida() - timedelta(hours = duracion + 2):
            return self._rutasFuturas[0].getFechaSalida() - timedelta(duracion + 2)

        # Viendo las colisiones con rutas asignadas.
        rutas = self._rutasFuturas
        for i in range(len(rutas) - 1):
            if rutas[i].getFechaLlegada() < rutas[i].getFechaSalida() - timedelta(hours = duracion + 2):
                return rutas[i].getFechaLlegada() + timedelta(hours = 1)

        # Si colisiona con todo el horario, se asigna una hora después del último lapso.
        return rutas[len(rutas) - 1].getFechaLleada() + timedelta(hours = 1)

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