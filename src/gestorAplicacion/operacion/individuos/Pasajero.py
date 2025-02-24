from Persona import Persona
from datetime import datetime

class Pasajero(Persona):
    _pasajeroRegistrados = []

    def __init__(self, nombre: str = "", edad: int = 0, id: int = 0,
                 maletas: list["Maleta"] = [], wallet: float = 0.0,
                 facturas: list["Factura"] = [], numReembolsoDisp: int = 0,
                 acompanante: Persona = None):
        super().__init__(nombre, edad, id)
        self._maletas = maletas
        self._wallet = wallet
        self._facturas = facturas
        self._numReembolsoDisp = numReembolsoDisp
        if acompanante != None:
            self._acompanante = acompanante
        Pasajero._pasajeroRegistrados.append(self)

    # Defiendo Getters y Setters ¡¡Los getters y Setters de nombre, edad y id ya se heredaron por Persona!!
    def getMaletas(self) -> list["Maleta"]:
        return self._maletas

    def getWallet(self) -> float:
        return self._wallet

    def getFacturas(self) -> list:
        return self._facturas

    def getNumReembolsoDisp(self) -> int:
        return self._numReembolsoDisp

    def getAcompanante(self) -> object:
        return self._acompanante

    def setMaletas(self, maletas: list["Maleta"]):
        from Maleta import Maleta

        self._maletas = []
        for maleta in maletas:
            if isinstance(maleta, Maleta):
                self._maletas.append(maleta)

    def setWallet(self, wallet: float):
        self._wallet = wallet

    def setFacturas(self, facturas: list):
        self._facturas = facturas

    def setNumReembolsoDisp(self, numReembolsoDisp: int):
        self._numReembolsoDisp = numReembolsoDisp

    def setAcompanante(self, acompanante: Persona):
        self._acompanante = acompanante
        Pasajero._pasajeroRegistrados.append(self)

    # Metodos de Clase
    @staticmethod
    def getPasajerosRegistrados():
        return Pasajero._pasajeroRegistrados

    @staticmethod
    def getCantidadPasajeros():
        return len(Pasajero._pasajeroRegistrados)

    @staticmethod
    def buscarPasajero(nombre: str = None, id: int = None) -> "Pasajero":
        """
        Busca un pasajero por nombre y/o ID.
        """
        for pasajero in Pasajero._pasajeroRegistrados:

            if nombre is not None and int(id) is not None:
                if pasajero.getNombre() == nombre and pasajero.getId() == int(id):
                    return pasajero
            elif nombre is not None and pasajero.getNombre() == nombre:
                return pasajero
            elif int(id) is not None and pasajero.getId() == int(id):
                return pasajero
        return None
    # Metodo de Instacia
    def mostrarDatos(self) -> str:
        return f"Soy el pasajero {self.getNombre()} tengo {self.getEdad()} años y mi ID es {self.getId()}"

    def revertirPasajes(self):
        facturas = self.getFacturas()
        if len(facturas) != 0 and facturas is not None:
            for factura in facturas:
                bus = factura.getRutaElegida().getBusAsociado()
                bus.asignarPasajero(self)

    def eliminarPasaje(self, factura: "Factura") -> str:
        facturas = self.getFacturas()
        if factura in facturas:
            facturas.remove(factura)
            return f"Pasajero {self.getNombre()} ha eliminado su factura {factura.getIdFactura()}"

    def solicitarReembolso(self, idPasajero: int, idFactura: int, horaZero: datetime) -> list:
        """
        Procesa una solicitud de reembolso.

        """

        from Contabilidad import Contabilidad


        idFacturaUser = int(idFactura)
        idPasajeroUser = int(idPasajero)
         # lo casteamos a int
        respuesta = []
        ratio = 86400.0 / 10.0  # 10 segundos reales = 1 día

        # Calculo la diferencia con la fecha de inicio del programa
        nowTime = datetime.now()  # Obtengo el tiempo exacto de solicitud

        # Diferencia en segundos reales
        segundosReales = (nowTime - horaZero).total_seconds()

        # Diferencia Simulada
        diferenciaZero = segundosReales * ratio
        mensaje = ""
        numReembolsoDispUser = (
            2  # usuario tiene 2 reembolsos disponibles por año
        )

        # Verificar si la diferencia es mayor a un año (en segundos)
        secondsInOneYear = 365 * 24 * 60 * 60  # 365 días en segundos
        if diferenciaZero > secondsInOneYear:
            numReembolsoDispUser = 2
        elif numReembolsoDispUser == 0:
            mensaje = "El Pasajero no tiene mas reembolsos por este ano, segun los terminos y condiciones"
            respuesta.append(mensaje)
            return respuesta

        facturas = Contabilidad.getVentas() 
        for factura in facturas:
            print(factura.getNombreUsuario())
            print(factura.getIdFactura())
            if factura.getIdFactura() == idFacturaUser:
                if factura.getIdUsuario() == idPasajeroUser:
                    timeCreation = (
                        factura._fecha
                    )  
                    

                    # Calcular la diferencia entre las fechas
                    diferencia = nowTime - timeCreation

                    if diferencia.total_seconds() / 3600 < 24:
                        mensaje = "El reembolso no puede hacerse efectivo, La diferencia no es mayor a 24 horas segun lo establecido por terminos y condiciones."
                        respuesta.append(mensaje)
                    elif (
                        factura.getMetodoPago() == "Efectivo"
                    ): 
                        mensaje = "El reembolso no es posible, el metodo de pago utilizado fue en efectivo, un metodo de pago invalido para un reembolso"
                        respuesta.append(mensaje)
                    else:
                        mensaje = "Su solicitud sigue en proceso, valoramos su paciencia y gracias por escojernos, ahora pasaremos a validar las maletas, Para esto ingrese los ID de las maletas"
                        # Actualizar el número de reembolsos disponibles
                        numReembolsoDispUser -= 1 
                        respuesta.append(mensaje)
                        respuesta.append(factura)
                        return respuesta
                else:
                    mensaje = "El documento no coincide con el del pasajero"
                    respuesta.append(mensaje)
                    return respuesta
        mensaje = "No existe Factura asociada al numero de la factura"
        respuesta.append(mensaje)
        return respuesta

    def registarAcompanante(self, nombre: str, id: int, edad: int) -> None:
        if edad >= 18:
            self.setAcompanante(Pasajero(nombre, edad, int))
        else:
            return "El acompañante debe ser mayor de edad."

    def comprarTiquete(self, rutaSeleccionada: "Ruta", metodoPago: int, horaZero: datetime):
        pass

    def aceptarCambio(self) -> bool:
        pass

    def pedirFactura(self):
        pass

    def agregarMaleta(self):
        pass

    def validarDestino(self):
        pass

    def validarHora(self):
        pass

    def proveerInformacion(self):
        pass
