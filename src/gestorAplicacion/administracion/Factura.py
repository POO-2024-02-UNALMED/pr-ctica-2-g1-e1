from datetime import datetime


class Factura:
    metodosDePago = [
        "Transferencia",
        "Tarjeta de Credito",
        "Tarjeta de Debito",
        "Efectivo",
    ]
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
    def getId(self):
        return self._idFactura

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
        bus = self.ruta_elegida.get_bus_asociado()
        if bus is not None:
            mensaje = "Existe un Bus Asociado a la ruta de la factura, Su solicitud seguira en proceso"
        else:
            mensaje = "Lo sentimos pero no existe bus Asociado a la ruta de dicha factura, por lo cual el reembolso no puede ser efectivo"
        
        return mensaje
    
    def verificarRutaAsociada(self):
        bus = self.ruta_elegida.get_bus_asociado()
        mensaje = ""

        asientos_bus = bus.get_asientos()
        for asiento in asientos_bus:
            if asiento.get_usuario().get_nombre() == self.usuario_nombre:
                mensaje = "El usuario ya tiene una reserva asociada a esta ruta"
                ruta_elegida = self.get_ruta_elegida()
                fecha_salida = ruta_elegida.get_fecha_salida()
                if datetime.now() < fecha_salida:
                    print("El asiento liberado puede ser reservado nuevamente, Su reembolso sigue en proceso")
                else:
                    print("Es demasiado tarde Para Hacer la reservacion, Proximamente el Bus saldra a su debida Ruta.")
            else:
                mensaje = "Lo sentimos, El usuario no tiene una reserva asociada a esta ruta"
        
        return mensaje
    

    def verificarMaletaBusAsociado(self, nums_maleta):
        bus = self.ruta_elegida.get_bus_asociado()
        verificacion = False
        for maleta in bus.get_equipaje():
            if maleta.get_id_maleta() == nums_maleta:
                verificacion = True
                break
        return verificacion
    
    def eliminarMaletaBusAsociado(self, nums_maletas):
        bus = self.ruta_elegida.get_bus_asociado()
        mensaje = ""
        
        for integer in nums_maletas:
            for maleta in bus.get_equipaje():
                if maleta.get_id_maleta() == integer:
                    bus.get_equipaje().remove(maleta)
                    mensaje = f"La maleta con el numero de identificacion {integer} ha sido eliminada del equipaje del bus"
                    break 
            else:
                mensaje = f"No se pudo hacer el reembolso, La maleta con el numero de identificacion {integer} no existe en el bus asociado a la factura"
        
        return mensaje

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
