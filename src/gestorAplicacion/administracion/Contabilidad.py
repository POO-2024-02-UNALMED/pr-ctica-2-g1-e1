from  gestorAplicacion.administracion.Factura import Factura
class Contabilidad:
    _costoCompensacion: int = 10
    _ventas: list = []
    _transacionesReembolsadas: list = []

    def __init__(self, ingresos: float = 0.0, costosOperativos: float = 0.0, ventas: list = [],
                 transacionesReembolsadas: list = []):
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

    @staticmethod
    def calcularTarifas(factura):
        tarifa_base = 5.0  
        porcentaje_reembolso = 0.02 * factura.get_valor()  # 2% descuento
        tarifa_por_metodo = 2.0 if factura.get_metodo_pago() == Factura.MetodoPagos.TarjetadeCredito else 0.0

        return tarifa_base + porcentaje_reembolso + tarifa_por_metodo

    @staticmethod
    def calcularDescuentos(factura):
        descuento = 0.0
        apariciones = 0
        
        for f in Contabilidad.get_ventas():
            if f.get_id_usuario() == factura.get_id_usuario():
                apariciones += 1

        if apariciones > 10:
            descuento += 0.1  # 10% descuento

        if factura.get_metodo_pago() == Factura.MetodoPagos.Transferencia:
            descuento += 0.05  #  5% adicional descuento

        return descuento

    @staticmethod
    def montoReembolso(factura):
        tarifas = Contabilidad.calcularTarifas(factura)  
        descuentos = Contabilidad.calcularDescuentos(factura)  
        monto_final = factura.getValor() - tarifas + descuentos
        return monto_final

    @classmethod
    def generarDesglose(cls, factura: object) -> str:
        tarifas: float = cls.calcularTarifas(factura)
        descuentos: float = cls.calcularDescuentos(factura)
        montoFinal: float = factura.getValor() - tarifas + descuentos
        return f""" Desglose de Reembolso:\n
                    Monto Base: ${factura.getValor()}
                    Tarifas Administrativas: ${tarifas}
                    Descuentos Aplicados: ${descuentos}
                    Monto Final Deesmbolso: ${montoFinal}"""

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
