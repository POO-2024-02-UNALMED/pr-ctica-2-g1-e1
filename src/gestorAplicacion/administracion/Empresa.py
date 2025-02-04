from gestorAplicacion.operacion.individuos.Chofer import Chofer
from gestorAplicacion.operacion.logistica.Bus import Bus

class Empresa:
    def __init__(
        self,
        nombre: str = "",
        empleados: list = [],
        buses: list = [],
        rutas: list = [],
        dineroEmpresa: float = 0.0,
        transaccionEmpresa: list = [],
    ):
        self._nombre = nombre
        self._empleados = empleados
        self._buses = buses
        self._rutas = rutas
        self._dineroEmpresa = dineroEmpresa

    # Definiendo Getters y Setters
    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEmpleados(self) -> list:
        return self._empleados

    def setEmpleados(self, empleados: list):
        self._empleados = empleados

    def getBuses(self) -> list:
        return self._buses

    def setBuses(self, buses: list):
        self._buses = buses

    def getRutas(self) -> list:
        return self._rutas

    def setRutas(self, rutas: list):
        self._rutas = rutas

    def getDineroEmpresa(self) -> float:
        return self._dineroEmpresa

    def setDineroEmpresa(self, dineroEmpresa: float):
        self._dineroEmpresa = dineroEmpresa

    # Metodos de Instacia
    def agregarEmpleado(self, empleado: Chofer):
        self._empleados.append(empleado)

    def contratarEmpleado(
        self,
        nombre: str = "",
        edad: int = 18,
        id: int = 0,
        sueldo: float = 0,
        horario: list = [],
    ):
        contratado = False
        if nombre == "":
            return "Se debe registrar un nombre."
        for empleado in self._empleados:
            if empleado.getNombre() == nombre:
                return "El empleado ya está contratado."
                break
        chofer = Chofer(nombre, edad, id, sueldo, self, horario)
        self._empleados.append(chofer)

    def despedirEmpleado(self, empleado: Chofer) -> str:
        for empleados in self._empleados:
            if empleados == empleado:
                self._empleados.remove(empleado)
                return f"Se ha despedido correctamente al chofer {empleado.getNombre()}"

    def comprarBus(self, bus:Bus, valor: int):
        if self._dineroEmpresa >= valor:
            self._dineroEmpresa -= valor
            
            return f"Se ha comprado el bus con éxito. Se queda con {self._dineroEmpresa}."
        else:
            return "No hay suficiente dinero para comprar el bus."

    def desvincularBus(self, bus: Bus):
        if bus == None:
            return "No se ha seleccionado un bus."
        for bus in self._buses:
            if bus == bus:
                self._buses.remove(bus)
                return f"Se ha desvinculado el bus {bus.getPlaca()} de la empresa."

    def asignarRutas(self, rutas: list):
        newRutas = self._rutas + rutas
        self._rutas = newRutas

    def reportarFinanzas(self):
        pass

    def reasignarPasajero(self):
        pass
