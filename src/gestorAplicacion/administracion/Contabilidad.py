class Contabilidad:
    _costoCompensacion: int = 10
    _ventas: list = []
    _transacionesReembolsadas: list = []

    def __init__(self, ingresos: float = 0.0, costosOperativos: float = 0.0, ventas: list["Factura"] = [],
                 transacionesReembolsadas: list = []):
        self._ingresos = ingresos
        self._costosOperativos = costosOperativos
        Contabilidad._ventas = ventas
        self._transacionesReembolsadas = transacionesReembolsadas

    # Definiendo Getters y Setters
    def getIngresos(self) -> float:
        return self._ingresos

    def getCostosOperativos(self) -> float:
        return self._costosOperativos

    def getVentas(cls) :
        return Contabilidad._ventas

    def getTransaccionesReembolsadas(self) -> list:
        return self._transacionesReembolsadas

    def setIngresos(self, ingresos):
        self._ingresos = ingresos

    def setCostosOperativos(self, costosOperativos):
        self._costosOperativos = costosOperativos

    def setVentas(self, ventas):
        from Factura import Factura

        self._ventas = []
        for venta in ventas:
            if isinstance(venta, Factura):
                self._ventas.append(venta)

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

    @staticmethod
    def calcularTarifas(factura: "Factura"):
        from Factura import Factura

        tarifa_base = 5.0  
        porcentaje_reembolso = 0.02 * factura.getValor()  # 2% descuento
        tarifa_por_metodo = 2.0 if factura.getMetodoPago() == "Tarjeta de Credito" else 0.0

        return tarifa_base + porcentaje_reembolso + tarifa_por_metodo

    @staticmethod
    def calcularDescuentos(factura: "Factura"):
        from Factura import Factura

        descuento = 0.0
        apariciones = 0
        
        for f in Contabilidad.getVentas():
            if f.getIdUsuario() == factura.getIdUsuario():
                apariciones += 1

        if apariciones > 10:
            descuento += 0.1  # 10% descuento

        if factura.getMetodoPago() == "Transferencia":
            descuento += 0.05  #  5% adicional descuento

        return descuento

    @staticmethod
    def montoReembolso(factura):
        tarifas = Contabilidad.calcularTarifas(factura)  
        descuentos = Contabilidad.calcularDescuentos(factura)  
        monto_final = factura.getValor() - tarifas + descuentos
        return monto_final

    @classmethod
    def generarDesglose(cls, factura: "Factura") -> str:
        tarifas: float = cls.calcularTarifas(factura)
        descuentos: float = cls.calcularDescuentos(factura)
        montoFinal: float = factura.getValor() - tarifas + descuentos
        return f""" Desglose de Reembolso:\n
                    Monto Base: ${factura.getValor()}
                    Tarifas Administrativas: ${tarifas}
                    Descuentos Aplicados: ${descuentos}
                    Monto Final Deesmbolso: ${montoFinal}"""

    @classmethod
    def calcularValorTiquete(cls, ruta: "Ruta") -> float:
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
