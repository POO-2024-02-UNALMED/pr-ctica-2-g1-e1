from Persona import Persona


class Pasajero(Persona):
    _pasajeroRegistrados = []

    def __init__(
        self,
        nombre: str = "",
        edad: int = 0,
        id: int = 0,
        maletas: list = [],
        wallet: float = 0.0,
        facturas: list = [],
        numReembolsoDisp: int = 0,
        acompanante: object = None,
    ):
        super.__init__(nombre, edad, id)
        self._maletas = maletas
        self._wallet = wallet
        self._facturas = facturas
        self._numReembolsoDisp = numReembolsoDisp
        if acompanante != None:
            self._acompanante = acompanante
            Pasajero._pasajeroRegistrados.append(self)

    # Defiendo Getters y Setters ¡¡Los getters y Setters de nombre, edad y id ya se heredaron por Persona!!
    def getMaletas(self) -> list:
        return self._maletas

    def getWallet(self) -> float:
        return self._wallet

    def getFacturas(self) -> list:
        return self._facturas

    def getNumReembolsoDisp(self) -> int:
        return self._numReembolsoDisp

    def getAcompanante(self) -> object:
        return self._acompanante

    def setMaletas(self, maletas: list):
        self._maletas = maletas

    def setWallet(self, wallet: float):
        self._wallet = wallet

    def setFacturas(self, facturas: list):
        self._facturas = facturas

    def setNumReembolsoDisp(self, numReembolsoDisp: int):
        self._numReembolsoDisp = numReembolsoDisp

    def setAcompanante(self, acompanante: object):
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
    def buscarPasajeroPorId(id: int) -> object:
        pass

    @staticmethod
    def buscarPasajeroPorNombre(nombre: str) -> object:
        pass

    # Metodo de Instacia
    def mostrarDatos(self):
        print(
            f"Soy el pasajero {self.getNombre()} tengo {self.getEdad()} años y mi ID es {self.getId()}"
        )

    def eliminarPasaje(self) -> str:
        pass

    def solicitarReembolso(self):
        pass

    def registarAcompanante(self):
        pass

    def comprarTiquete(self):
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
