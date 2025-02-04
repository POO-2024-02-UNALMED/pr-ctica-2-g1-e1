class Maleta:
    _maletas = []

    def __init__(self, propietario: object = None, peso: int = 0):
        self._idMaleta = len(Maleta._maletas) + 1
        self.propietario = propietario
        self.peso = peso

    # Definiendo Getters y Setters
    def getIdMaleta(self):
        return self._idMaleta

    def getPropietario(self):
        return self.propietario

    def setPropietario(self, value):
        self.propietario = value

    def getPeso(self):
        return self.peso

    def setPeso(self, value):
        self.peso = value

    # Metodos de Instancia
    def mostrarDetalles(self):
        pass

    def asociarPropietario(self):
        pass

    def comprobarLimitePeso(self):
        pass

    # Metodos Estaticos
    @staticmethod
    def getCantidadMaletas(self):
        return len(Maleta._maletas)

    @staticmethod
    def agregarMaleta(maleta: "Maleta"):
        Maleta._maletas.append(maleta)

    @staticmethod
    def eliminarMaleta(idMaleta: int):
        for maleta in Maleta._maletas:
            if maleta.getIdMaleta() == idMaleta:
                Maleta._maletas.remove(maleta)
                return True
        return False
