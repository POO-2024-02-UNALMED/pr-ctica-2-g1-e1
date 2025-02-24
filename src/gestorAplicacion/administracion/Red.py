from abc import ABC, abstractmethod

class Red(ABC):
    PARADAS = ["BOGOTA", "MEDELLIN", "BARRANQUILLA", "CALI", "PEREIRA", "TUNJA",
               "VILLAVICENCIO", "CARTAGENA", "IBAGUE", "PASTO"]

    # Construyendo la red de carreteras.
    CARRETERAS = []
    """
    Creación de la red de carreteras:
    Esta vendrá representada por un grafo.
    Los vértices serán las paradas (Representadas por su ordinal).
    Las aristas serán representadas por una tupla, cuyas entradas:
        ((a11, a12), t)
    Significan:
        a11, a12 son las paradas,
        t es el tiempo de recorrido entre las trayecto (En minutos).
 
    Se supondrá que el tiempo y distancia entre trayecto es la misma en ambas direcciones de recorrido.
    Téngase en cuenta que la enumeración de ciudades está dada por:
        0. Bogota
        1. Medellin
        2. Barranquilla
        3. Cali
        4. Pereira
        5. Tunja
        6. Villavicencio
        7. Cartagena
        8. Ibagué
        9. Pasto

    Finalmente se calculan todas las distancias mínimas entre trayecto.
    """
 
    CARRETERAS.append(((0, 1), 500))
    CARRETERAS.append(((0, 2), 1100))
    CARRETERAS.append(((0, 5), 130))
    CARRETERAS.append(((0, 6), 170))
    CARRETERAS.append(((0, 7), 1110))
    CARRETERAS.append(((0, 8), 240))
    CARRETERAS.append(((0, 9), 1110))
    CARRETERAS.append(((1, 2), 800))
    CARRETERAS.append(((1, 4), 330))
    CARRETERAS.append(((1, 5), 530))
    CARRETERAS.append(((1, 7), 730))
    CARRETERAS.append(((2, 4), 1050))
    CARRETERAS.append(((2, 5), 1110))
    CARRETERAS.append(((2, 7), 1110))
    CARRETERAS.append(((2, 8), 1040))
    CARRETERAS.append(((3, 4), 200))
    CARRETERAS.append(((3, 8), 290))
    CARRETERAS.append(((3, 9), 520))
    CARRETERAS.append(((4, 8), 170))
    CARRETERAS.append(((5, 7), 1000))
    CARRETERAS.append(((7, 8), 1140))
    

    # Hallando las distancias mínimas para cada trayecto.
    DISTANCIAS = []
    for i in range(len(PARADAS)):
        DISTANCIAS.append([100000 for _1 in range(len(PARADAS))])
        # Iniciando la matriz de pesos.
    for arista in CARRETERAS:
        DISTANCIAS[arista[0][0]][arista[0][1]] = arista[1]
        DISTANCIAS[arista[0][1]][arista[0][0]] = arista[1]
    # Algoritmo de Floyd-Warshall.
    for k in range(len(PARADAS)):
        for i in range(len(PARADAS)):
            for j in range(len(PARADAS)):
                DISTANCIAS[i][j] = min(DISTANCIAS[i][j], DISTANCIAS[i][k] + DISTANCIAS[k][j])

    def Parada(i: int):
        # Devuelve la parada en la posición i-ésima.
        return Red.PARADAS[i]

    @classmethod
    def ordinal(cls, parada: str) -> int:
        # Dada una ciudad, regresa su posición en el array PARADAS.
        def simplificarPalabra(palabra: str) -> str:
            # Se quitan todas las tildes y se pone en minúscula una palabra.
            palabra = palabra.lower()
            palabra = palabra.replace("á", "a")
            palabra = palabra.replace("é", "e")
            palabra = palabra.replace("í", "i")
            palabra = palabra.replace("ó", "o")
            palabra = palabra.replace("ú", "u")

            return palabra

        for i in range(len(cls.PARADAS)):
            if simplificarPalabra(parada) == simplificarPalabra(cls.PARADAS[i]):
                return i

    @classmethod
    def posicion(cls, trayecto: list[int], ordinal: int) -> tuple[int]:
        """
        Dado un conjunto de trayecto y una parada extra (Ordinales), se mira dónde
        debería ir la parada extra en el conjunto de trayecto para así
        minimizar la distancia total en caso de añadir la parada extra.

        Parámetros:
            - trayecto: list[int],
                Conjunto de ordinales de las PARADAS en el trayecto.
            - parada: int,
                Ordinal de la parada a averiguar su posición óptima.

        Retorna:
            - posiciones, tuple[int].
                Las posiciones de la parada anterior y siguiente
                en la ruta donde se optimiza la posición de la nueva parada.
        """

        # Tomando el tamaño del trayecto.
        longitud = len(trayecto)

        # Trata de errores.
        if (longitud < 1) or (longitud < 0) or (longitud > len(Red.PARADAS)):
            return None
        
        # Encontrando dónde se minimiza la distancia.
        distanciaMinima = 100000
        posicionMinima  = 0
        for i in range(longitud):
            # Viendo que el punto no esté en el trayecto.
            if Red.DISTANCIAS[ordinal][trayecto[i]] == 0:
                return None
            
            # Viendo si la distancia a este punto es menor a las anteriores.
            if distanciaMinima > Red.DISTANCIAS[ordinal][trayecto[i]]:
                distanciaMinima = Red.DISTANCIAS[ordinal][trayecto[i]]
                posicionMinima = i

        # Viendo si es mejor poner la parada antes o después de la posición i.
        distanciaAnterior, distanciaPosterior = 0, 0 # Distancias.
        anterior, minima, posterior = 0, trayecto[posicionMinima], 0 # Ordinales.

        if posicionMinima == 0:
            posterior = trayecto[1]

            # Distancia agregando la nueva parada al inicio.
            distanciaAnterior = Red.DISTANCIAS[ordinal][minima] + Red.DISTANCIAS[minima][posterior]

            # Distancia agregando la nueva parada entre la primera y segunda parada.
            distanciaPosterior = Red.DISTANCIAS[minima][ordinal] + Red.DISTANCIAS[ordinal][posterior]
        elif posicionMinima == longitud - 1:
            anterior = trayecto[longitud - 2]

            # Distancia agregando la nueva parada entre la penúltima y última parada.
            distanciaAnterior = Red.DISTANCIAS[anterior][ordinal] + Red.DISTANCIAS[ordinal][minima]

            # Distancia agregando la nueva parada al final.
            distanciaPosterior = Red.DISTANCIAS[anterior][minima] + Red.DISTANCIAS[minima][ordinal]
        else:
            anterior = trayecto[posicionMinima - 1]
            posterior = trayecto[posicionMinima + 1]

            # Distancia agregando la nueva parada en medio.
            distanciaAnterior = Red.DISTANCIAS[anterior][ordinal] + Red.DISTANCIAS[ordinal][minima] + Red.DISTANCIAS[minima][posterior]

            # Distancia agregando la nueva parada después.
            distanciaPosterior = Red.DISTANCIAS[anterior][minima] + Red.DISTANCIAS[minima][ordinal] + Red.DISTANCIAS[ordinal][posterior]

        # Devolviendo las posiciones óptimas.
        if distanciaAnterior > distanciaPosterior:
            return (posicionMinima, posicionMinima + 1)
        else:
            return (posicionMinima - 1, posicionMinima)

    @classmethod
    def algoritmoBellmanFord(cls, paradaInicio: int, paradaFinal: int) -> list[int]:
        """
        Devuelve la ruta más corta dada la función de pesos entre los vértices de origen y llegada.

        Parámetros:
            - verticeInicial: int,
                El vértice inicial de la ruta.
            - verticeFinal: int,
                El vértice final de la ruta.

        Retorna:
            - ordinalesRutaOptima: list[int],
                El trayecto que optimiza la distancia asociada a los pesos entre los vértices
                inicial y final, pero indicando el ordinal de cada parada.
        """

        # Se establece el predecesor en la ruta.
        # Y su distancia desde el origen.
        padres = [-1] * len(Red.PARADAS)
        recorrido = [100000] * len(Red.PARADAS)
        recorrido[paradaInicio] = 0

        # Implementando el algoritmo de BellmaFord.
        for i in range(len(Red.PARADAS)):
            for arista in Red.CARRETERAS:
                vertice1 = arista[0][0]
                vertice2 = arista[0][1]
                peso = arista[1]

                # Comparando si es mejor cambiar el camino hacia el vértice 2 pasando por el vértice 1
                if(recorrido[vertice2] > recorrido[vertice1] + peso):
                    recorrido[vertice2] = recorrido[vertice1] + peso
                    padres[vertice2] = vertice1

                # Viceversa:
                if(recorrido[vertice1] > recorrido[vertice2] + peso):
                    recorrido[vertice1] = recorrido[vertice2] + peso
                    padres[vertice1] = vertice2

        # Construcción de paradas intermedias.
        parada = paradaFinal
        paradas = [parada]
        while(padres[parada] != -1):
            # Añadiendo al padre a la lista.
            paradas.insert(0, padres[parada])

            # Inducción.
            parada = padres[parada]

        # Retornando las paradas.
        return paradas

    @classmethod
    def ordenarParadas(cls, trayecto: list[int]) -> list[int]:
        """
        Ordena las paradas de tal manera que el orden represente un recorrido que optimiza la distancia total.

        Parámetros:
            - trayecto: list[int],
                Conjunto original de paradas (ordinales).

        Retorna:
            - paradasOrdenadas: list[int],
                Paradas (ordinales) organizadas para minimizar el orden.
        """

        # Verificación de errores.
        if trayecto is None:
            return []
        elif len(trayecto) <= 1:
            return trayecto

        # Creando el array que ordenará las paradas.
        paradasOrdenadas = trayecto[0: 2]

        # Ordenando.
        for i in range(2, len(trayecto)):
            # Viendo la posición del elemento i-ésimo.
            posiciones = cls.posicion(paradasOrdenadas, trayecto[i])

            if posiciones is not None:
                paradasOrdenadas.insert(posiciones[0] + 1, trayecto[i])

        # Retornando.
        return paradasOrdenadas

    @classmethod
    def agregarParada(cls, trayecto: list[int], ordinal: int) -> list[int]:
        """
        Añade la nueva parada haciendo minimizando su efecto en la ruta.

        Parámetros:
            - trayecto: list[int],
                Conjunto de ordinales paradas en donde se va a añadir la nueva parada.
            - ordinal: int,
                Ordinal de la parada a añadir.

        Retorna:
            - nuevoTrayecto: list[int],
                El resultado de agregar la nueva parada.
        """

        # Corrección de errores.
        if len(trayecto) < 2:
            return "Error"
        
        #
        posiciones = cls.posicion(trayecto, ordinal)
        if posiciones is None:
            return trayecto

        # Colocando el nuevo valor.
        nuevoTrayecto = trayecto.copy()
        nuevoTrayecto.insert(posiciones[0] + 1, ordinal)

        return nuevoTrayecto

    @classmethod
    def eliminarParada(cls, trayecto: list[int], ordinal: int) -> list[int]:
        nuevoTrayecto = trayecto.copy()
        if ordinal in nuevoTrayecto:
            nuevoTrayecto.remove(ordinal)

        return nuevoTrayecto

    @classmethod
    def longitud(cls, trayecto: list[int]) -> int:
        """
        Retorna la duración temporal de un trayecto.

        Parámetros:
            - ordinalesTrayecto: int[],
                Conjunto de paradas (Ordinales) a calcular su longitud.

        Retorna:
            - tiempo: int,
                Duración del trayecto.
        """

        # Ordenando la lista.
        trayecto = cls.ordenarParadas(trayecto)

        # Calculando el tiempo.
        tiempo = 0
        for i in range(len(trayecto) - 1):
            actual, siguiente = trayecto[i], trayecto[i + 1]
            tiempo += cls.DISTANCIAS[actual][siguiente]

        # Retornando.
        return tiempo