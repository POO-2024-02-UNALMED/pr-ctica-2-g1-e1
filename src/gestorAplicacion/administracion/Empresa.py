from gestorAplicacion.operacion.individuos.Chofer import Chofer
from gestorAplicacion.operacion.logistica.Bus import Bus
from gestorAplicacion.administracion.Ruta import Ruta

import random
from datetime import timedelta

class Empresa:
    def __init__(self, nombre: str = "", empleados: list = [],
                 buses: list = [], rutas: list = [], dineroEmpresa: float = 0.0,
                 transaccionEmpresa: list = []):
        self._nombre = nombre
        self.setEmpleados(empleados)
        self.setBuses(buses)
        self.setRutas(rutas)
        self._dineroEmpresa = dineroEmpresa

    # Definiendo Getters y Setters
    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEmpleados(self) -> list[Chofer]:
        return self._empleados

    def setEmpleados(self, empleados: list[Chofer]):
        self._empleados = []
        for empleado in empleados:
            if empleado not in self._empleados:
                self.agregarEmpleado(empleado)

    def getBuses(self) -> list[Bus]:
        return self._buses

    def setBuses(self, buses: list[Bus]):
        self._buses = []
        for bus in buses:
            if isinstance(bus, Chofer):
                self._buses.append(bus)

    def getRutas(self) -> list[Ruta]:
        return self._rutas

    def setRutas(self, rutas: list[Ruta]):
        self._rutas = []
        for ruta in rutas:
            if isinstance(ruta, Ruta) and ruta not in self._rutas:
                self._rutas.append(ruta)

    def getDineroEmpresa(self) -> float:
        return self._dineroEmpresa

    def setDineroEmpresa(self, dineroEmpresa: float):
        self._dineroEmpresa = dineroEmpresa

    # Metodos de Instacia
    def agregarEmpleado(self, empleado: Chofer):
        if isinstance(empleado, Chofer) and empleado not in self._empleados:
            self._empleados.append(empleado)
            empleado.setEmpresa(self)

    def contratarEmpleado(self, chofer: Chofer = None, sueldo: int = None, horario: list = []):
        """
        Agrega un chofer a la nómina.

        Parámetros:
            - chofer: Chofer,
                Persona a contratar.
            - sueldo: int,
                Sueldo ofrecido para contratar.
            - horario: ArrayList<LocalDateTime[]>,
                Horario con el que va a iniciar.
        """

        # Generando un sueldo en caso de no ser especificado.
        if sueldo is None: sueldo = 1000 + random.randrange(-10, 10) * 10

        # Generando un chofer aleatorio en caso de no ser especificado.
        if chofer is None:
            edad = 18 + random.randrange(0, 10)
            chofer = Chofer(edad = edad, horario = horario)

        # Estableciendo el contrato.
        if chofer.getEmpresa() != None:
            chofer.getEmpresa().despedirEmpleado(chofer)
            chofer.setEmpresa(self)
        self.agregarEmpleado(chofer)
        chofer.setSueldo(sueldo)

    def despedirEmpleado(self, empleado: Chofer):
        """
        Quita al chofer indicado de la nómina.

        Parámetros:
            - chofer: Chofer,
                Empleado a despedir.
        """

        # Haciendo el despido.
        self._empleados.remove(empleado)
        if empleado.getEmpresa() == self:
            empleado.setEmpresa(None)

    def agregarBus(self, bus: Bus, rutasFuturas: list[Ruta] = []):
        if bus.getEmpresa() is not None:
            bus.getEmpresa().desvincularBus(bus)
        if isinstance(bus, Bus) and bus not in self._buses:
            self._buses.append(bus)
        
        bus.setRutasFuturas(rutasFuturas)

    def comprarBus(self, valor: int, bus: Bus = None, rutasFuturas: list[Ruta] = []) -> str:
        """
        Agrega un bus a las utilidades.

        Parámetros:
            - bus: Bus,
                Bus a comprar.
            - valor: int,
                Costo del bus.
            - rutasFuturas: ArrayList<Ruta>,
                Rutas con el que va a iniciar.
        """

        # Verificando si se puede comprar el bus.
        if self._dineroEmpresa >= valor:
            self._dineroEmpresa -= valor

            # Creando un bus en caso de no haberse especificado.
            if bus is None:
                bus = Bus(rutasFuturas = rutasFuturas)

            if isinstance(bus, Bus):
                # Desvinculando el bus en otra empresa, si es que se la compró.
                if bus.getEmpresa() is not None:
                    bus.getEmpresa().setDineroEmpresa(bus.getEmpresa().getDineroEmpresa() + valor)
                    bus.getEmpresa().desvincularBus(bus)
                # Haciendo el cambio.
                if bus not in self._buses:
                    self._buses.append(bus)
                    bus.setEmpresa(self)
                    bus.setRutasFuturas(rutasFuturas)

            return f"Se ha comprado el bus con éxito. Se queda con {self._dineroEmpresa}."
        else:
            return "No hay suficiente dinero para comprar el bus."

    def desvincularBus(self, bus: Bus):
        """
        Quita al bus vinculado a la empresa.
 
        Parámetros:
            - bus: Bus,
                Bus a desvincular.
        """

        if isinstance(bus, Bus):
            # Quitando al bus de la nómina.
            self._buses.remove(bus)
            bus.setEmpresa(None)

            # Haciendo que todas sus rutas queden disponibles para otros buses.
            for ruta in bus.getRutasFuturas():
                ruta.setBus(None)

    def asignarRuta(self, ruta: Ruta):
        """
        Dado una ruta establecida, se busca el bus que tiene un horario disponible que
        cumpla las horas establecidas por la ruta. Dentro de esto, se escoge el que
        su horario de disponibilidad esté más cercano.

        Parámetros:
            - ruta: Ruta,
                Ruta a ser asignada.

        Retorna:
            - busEncontrado: Bus,
                Bus que va a tener esa ruta.
        """

        # Viendo si existen buses a los cuales asignar la ruta.
        if len(self._buses) != 0:
            # Generar precio aleatorio para comprar un bus nuevo.
            precioAleatorio = random.randrange(0, 10) * 1000 + 17000
            self.comprarBus(precioAleatorio)

        # Viendo la duración de la ruta.
        duracion = ruta.getTiempoEstimado()

        # Estableciendo una cota a la fecha.
        horarioBusBase = self._buses[0] 
        busEncontrado = self._buses[0]

        # Buscando la fecha más cercana con un bus disponible.
        for bus in self._buses:
            horarioBus = bus.hallarHueco(duracion)
            if horarioBusBase > horarioBus:
                horarioBusBase = horarioBus
                busEncontrado = bus

        # Asignando la ruta al bus.
        ruta.setFechaSalida(horarioBusBase)
        ruta.setFechaLlegada(horarioBusBase + timedelta(hours = duracion))
        busEncontrado.anadirRuta(ruta)

        # Buscando un chofer para que la conduzca.
        if ruta.getChoferAsociado() is not None:
            return None
        for empleado in self._empleados:
            if empleado.isDisponible(ruta.getFechaSalida(), ruta.getFechaLlegada()):
                retorno = empleado.anadirRuta(ruta.getFechaSalida(), ruta.getFechaLlegada())
                if retorno is None:
                    ruta.setChoferAsociado(empleado)
                    break
        else:
            self.contratarEmpleado(horario = (ruta.getFechaSalida(), ruta.getFechaLlegada()))
            ruta.setChoferAsociado(self._empleados[-1])

    def reasignarPasajero(self):
        pass
