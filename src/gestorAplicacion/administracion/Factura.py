from datetime import datetime


class Factura:
    metodosDePago = {
        "efectivo": "Efectivo",
        "tarjetaCredito": "Tarjeta de Crédito",
        "tarjetaDebito": "Tarjeta de Débito",
        "Transferencia": "Transferencia",
    }
    _cantidadFacturas = []

    def __init__(
        self,
        nombreUsuario: str = "",
        idUsuario: int = 0,
        valor: float = 0.0,
        numAsientosAsignados: int = 0,
        asientosAsignados: list = [],
        fecha: datetime = datetime.now(),
        cantidadMaletas: int = 0,
        rutaElegida: object = None,
        origen: str = "",
        destino: str = "",
        metodoPago: str = None,
    ):
        self._idFactura = len(Factura._cantidadFacturas) + 1
        self._nombreUsuario = nombreUsuario
        self._idUsuario = idUsuario
        self._valor = valor
        self._numAsientosAsignados = numAsientosAsignados
        self._asientosAsignados = asientosAsignados
        self._fecha = fecha
        self._cantidadMaletas = cantidadMaletas
        self._rutaElegida = rutaElegida
        self._origen = origen
        self._destino = destino
        self._metodoPago = metodoPago
        self._cantidadFacturas.append(self)

    # Definiendo Getters y Setters
    def getNombreUsuario(self) -> str:
        return self._nombreUsuario

    def getIdUsuario(self) -> int:
        return self._idUsuario

    def getValor(self) -> float:
        return self._valor

    def getNumAsientosAsignados(self) -> int:
        return self._numAsientosAsignados

    def getAsientosAsignados(self) -> list:
        return self._asientosAsignados

    def getFecha(self) -> datetime:
        return self._fecha

    def getCantidadMaletas(self) -> int:
        return self._cantidadMaletas

    def getRutaElegida(self) -> object:
        return self._rutaElegida

    def getOrigen(self) -> str:
        return self._origen

    def getDestino(self) -> str:
        return self._destino

    def getMetodoPago(self) -> str:
        return self._metodoPago

    def getMetodosDePago(self) -> dict:
        return Factura.metodosDePago

    def getIdFactura(self) -> int:
        return self._idFactura

    def setNombreUsuario(self, nombreUsuario: str):
        self._nombreUsuario = nombreUsuario

    def setIdUsuario(self, idUsuario: int):
        self._idUsuario = idUsuario

    def setValor(self, valor: float):
        self._valor = valor

    def setNumAsientosAsignados(self, numAsientosAsignados: int):
        self._numAsientosAsignados = numAsientosAsignados

    def setAsientosAsignados(self, asientosAsignados: list):
        self._asientosAsignados = asientosAsignados

    def setFecha(self, fecha: datetime):
        self._fecha = fecha

    def setCantidadMaletas(self, cantidadMaletas: int):
        self._cantidadMaletas = cantidadMaletas

    def setRutaElegida(self, rutaElegida: object):
        self._rutaElegida = rutaElegida

    def setOrigen(self, origen: str):
        self._origen = origen

    def setDestino(self, destino: str):
        self._destino = destino

    def setMetodoPago(self, metodoPago: str):
        self._metodoPago = metodoPago

    # Métodos de clase
    # Métodos de Instancia
    def verificarBusAsociado(self):
        pass

    def verificarRutaAsociada(self):
        pass

    def verificarMaletaBusAsociado(self) -> bool:
        pass

    def imprimirFactura(self) -> str:
        return f"""
               ================================================================
                                    Reporte Factura Comprada
               ================================================================
               Factura: {self.getIdFactura()}
               Usuario: {self.getNombreUsuario()}
               Valor: {self.getValor()}
               Origen: {self.getOrigen()}
               Destino: {self.getDestino()}
               Fecha: {self.getFecha()}
               """

    def AplicarDescuento():
        pass

    def asientoAsignado():
        pass

    def cantidadMaletas():
        pass

    def verificarEdad():
        pass
