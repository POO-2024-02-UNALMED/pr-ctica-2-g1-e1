class Maleta:
    _maletas = []
    _MAX_PESO_MALETA = [500, 1500, 3000, 5000]

    def __init__(self, propietario: "Pasajero" = None, peso: int = 0):
        self._idMaleta = len(Maleta._maletas) + 1
        self.propietario = propietario
        self.peso = peso
        Maleta._maletas.append(self)

    # Definiendo Getters y Setters
    def getIdMaleta(self):
        return self._idMaleta

    def getPropietario(self):
        return self.propietario

    def setPropietario(self, pasajero: "Pasajero"):
        from Pasajero import Pasajero

        if isinstance(pasajero, Pasajero):
            self.propietario = pasajero

    def getPeso(self):
        return self.peso

    def setPeso(self, value):
        self.peso = value

    # Metodos de Instancia
    def mostrarDetalles(self) -> str:
        return f""" Maleta Nro: {self.getIdMaleta()}
                    Propietario: {self.propietario.getNombre()}
                    Peso: {self.peso} kg"""

    def comprobarLimitePeso(self, peso: int) -> str:
        if peso > Maleta._MAX_PESO_MALETA[3]:
            return "El peso de la maleta supera el límite máximo."
        elif peso > Maleta._MAX_PESO_MALETA[2]:
            return "El peso de la maleta está en el rango pesado."
        elif peso > Maleta._MAX_PESO_MALETA[1]:
            return "El peso de la maleta está en el rango medio."
        elif peso > Maleta._MAX_PESO_MALETA[0]:
            return "El peso de la maleta está en el rango ligero."
        else:
            return "El peso de la maleta está en el rango extra ligero."

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
