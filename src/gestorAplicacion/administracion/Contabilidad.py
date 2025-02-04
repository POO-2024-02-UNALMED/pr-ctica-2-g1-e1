class Contabilidad:
    _costoCompensacion: int = 10
    _ventas: list = []
    _transacionesReembolsadas: list = []

    def __init__(
        self,
        ingresos: float = 0.0,
        costosOperativos: float = 0.0,
        ventas: list = [],
        transacionesReembolsadas: list = [],
    ):
        self._ingresos = ingresos
        self._costosOperativos = costosOperativos
        self._ventas = ventas
        self._transacionesReembolsadas = transacionesReembolsadas

    # Definiendo Getters y Setters
    def getIngresos(self) -> float:
        return self._ingresos

    def getCostosOperativos(self) -> float:
        return self._costosOperativos

    def getVentas(self) -> list:
        return self._ventas

    def getTransaccionesReembolsadas(self) -> list:
        return self._transacionesReembolsadas

    def setIngresos(self, ingresos):
        self._ingresos = ingresos

    def setCostosOperativos(self, costosOperativos):
        self._costosOperativos = costosOperativos

    def setVentas(self, ventas):
        self._ventas = ventas

    def setTransaccionesReembolsadas(self, transaccionesReembolsadas):
        self._transaccionesReembolsadas = transaccionesReembolsadas

    # Métodos de clase
    @classmethod
    def getVentas(cls) -> list:
        return cls._ventas

    @classmethod
    def setVentas(cls, ventas):
        cls._ventas = ventas

    @classmethod
    def getCostoCompensacion(cls) -> int:
        return cls._costoCompensacion

    @classmethod
    def setCostoCompensacion(cls, costoCompensacion):
        cls._costoCompensacion = costoCompensacion

    @classmethod
    def anadirVenta(cls, venta: object):
        cls._ventas.append(venta)

    @classmethod
    def anadirTransaccionReembolsada(cls, transaccionReembolsada: object):
        cls._transaccionesReembolsadas.append(transaccionReembolsada)

    @classmethod
    def calcularCostoCompensacion(cls, numeroPasajeros: int) -> float:
        return cls._costoCompensacion * numeroPasajeros

    @classmethod
    def calcularTarifas(cls, factura: object) -> float:
        pass

    @classmethod
    def calcularDescuentos(cls, factura: object) -> float:
        pass

    @classmethod
    def montoReembolso(cls, factura: object) -> float:
        pass

    @classmethod
    def calcularDesglose(cls, factura: object) -> str:
        tarifas: float = cls.calcularTarifas(factura)
        descuentos: float = cls.calcularDescuentos(factura)
        montoFinal: float = factura.getValor() - tarifas + descuentos
        return f"""
            Desglose de Reembolso:\n
            Monto Base: ${factura.getValor()}
            Tarifas Administrativas: ${tarifas}
            Descuentos Aplicados: ${descuentos}
            Monto Final Deesmbolso: ${montoFinal}
            """

    @classmethod
    def calcularValorTiquete(cls, ruta: object) -> float:
        pass

    # Metodos de Instancia
    def reportarFinanzas(self, costoCompensacion: int, facturas: list) -> list:
        pass

    def calcularIngresosTotales(self, facturas: list) -> float:
        pass

    def procesarReembolso(self, factura: object):
        pass

    def pagarMantenimiento(self):
        pass

    def pagarEmpleado(self):
        pass
