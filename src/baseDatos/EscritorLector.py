import pickle

def guardar_datos(datos, nombreArchivo):
    """
    Guarda los datos en un archivo utilizando pickle.

    Argumentos:
        datos: Los datos a guardar (cualquier objeto serializable).
        nombreArchivo: El nombre del archivo donde guardar los datos.
    """

    try:
        with open(nombreArchivo, 'wb') as archivo:
            pickle.dump(datos, archivo)
        print(f"Datos guardados en '{nombreArchivo}'")
        # El archivo se cierra automáticamente aquí no hace falta especificarlo
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos(nombreArchivo):
    """
    Carga los datos desde un archivo utilizando pickle.

    Argumentos:
        nombreArchivo: El nombre del archivo desde donde cargar los datos.
        
    Retorno:
        Los datos cargados, o None si ocurre un error.
    """
    try:
        with open(nombreArchivo, 'rb') as archivo:
            datos = pickle.load(archivo)
        print(f"Datos cargados desde '{nombreArchivo}'")
        # El archivo se cierra automáticamente aquí no hace falta especificarlo
        return datos
    except FileNotFoundError:
        print(f"Archivo '{nombreArchivo}' no encontrado.")
        return None
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None


"""

La idea es la siguiente muchachos ojo,
que si tienes un objeto que quieres guardar
y luego recuperar, puedes hacerlo de la siguiente manera:


1. Primero creas el objeto aqui abajo seguido, la idea es separar los objetos segun sus clases pasajeros, rutas, etc etc
2. Luego creas la variable con el nombre del archivo (utilicen el path que ya esta escrito) lo pasas a la función guardar_datos 
3. creas una variable para cargar los datos
4 todo gud 

"""
def LlamarBDRuta():
        # rutas_data.py
    from Ruta import Ruta
    from Bus import Bus
    from Chofer import Chofer
    from Empresa import Empresa
    from datetime import datetime, timedelta

    rutas = []

    # Crear objetos Bus
    bus1 = Bus(placa="ABC-123", cantidadAsientos=30, pesoMaximo=500, estado="Perfecto Estado")
    bus2 = Bus(placa="DEF-456", cantidadAsientos=40, pesoMaximo=750, estado="Necesita Reparación")
    bus3 = Bus(placa="GHI-789", cantidadAsientos=35, pesoMaximo=1000, estado="Perfecto Estado")
    bus4 = Bus(placa="JKL-012", cantidadAsientos=45, pesoMaximo=1250, estado="En Mantenimiento")
    bus5 = Bus(placa="MNO-345", cantidadAsientos=30, pesoMaximo=500, estado="Perfecto Estado")
    bus6 = Bus(placa="PQR-678", cantidadAsientos=40, pesoMaximo=750, estado="Necesita Reparación")
    bus7 = Bus(placa="STU-901", cantidadAsientos=35, pesoMaximo=1000, estado="Perfecto Estado")
    bus8 = Bus(placa="VWX-234", cantidadAsientos=45, pesoMaximo=1250, estado="En Mantenimiento")
    bus9 = Bus(placa="YZA-567", cantidadAsientos=30, pesoMaximo=500, estado="Perfecto Estado")
    bus10 = Bus(placa="BCD-890", cantidadAsientos=40, pesoMaximo=750, estado="Necesita Reparación")
    bus11 = Bus(placa="EFG-123", cantidadAsientos=35, pesoMaximo=1000, estado="Perfecto Estado")
    bus12 = Bus(placa="HIJ-456", cantidadAsientos=45, pesoMaximo=1250, estado="En Mantenimiento")
    bus13 = Bus(placa="KLM-789", cantidadAsientos=30, pesoMaximo=500, estado="Perfecto Estado")
    bus14 = Bus(placa="NOP-012", cantidadAsientos=40, pesoMaximo=750, estado="Necesita Reparación")
    bus15 = Bus(placa="QRS-345", cantidadAsientos=35, pesoMaximo=1000, estado="Perfecto Estado")
    bus16 = Bus(placa="TUV-678", cantidadAsientos=45, pesoMaximo=1250, estado="En Mantenimiento")
    bus17 = Bus(placa="WXY-901", cantidadAsientos=30, pesoMaximo=500, estado="Perfecto Estado")
    bus18 = Bus(placa="ZAB-234", cantidadAsientos=40, pesoMaximo=750, estado="Necesita Reparación")
    bus19 = Bus(placa="CDE-567", cantidadAsientos=35, pesoMaximo=1000, estado="Perfecto Estado")
    bus20 = Bus(placa="FGH-890", cantidadAsientos=45, pesoMaximo=1250, estado="En Mantenimiento")

    # Crear objetos Chofer
    chofer1 = Chofer(nombre="Carlos Pérez", edad=40, id=1001)
    chofer2 = Chofer(nombre="Ana Gómez", edad=35, id=1002)
    chofer3 = Chofer(nombre="Luis Martínez", edad=45, id=1003)
    chofer4 = Chofer(nombre="Sofía Díaz", edad=38, id=1004)
    chofer5 = Chofer(nombre="Andrés Sánchez", edad=42, id=1005)
    chofer6 = Chofer(nombre="Valentina Torres", edad=39, id=1006)
    chofer7 = Chofer(nombre="Diego Ramírez", edad=41, id=1007)
    chofer8 = Chofer(nombre="Isabella Vargas", edad=37, id=1008)
    chofer9 = Chofer(nombre="Mateo Castro", edad=43, id=1009)
    chofer10 = Chofer(nombre="Camila Herrera", edad=36, id=1010)
    chofer11 = Chofer(nombre="Sebastián Rodríguez", edad=44, id=1011)
    chofer12 = Chofer(nombre="Daniela Jiménez", edad=39, id=1012)
    chofer13 = Chofer(nombre="Nicolás Silva", edad=40, id=1013)
    chofer14 = Chofer(nombre="Gabriela Torres", edad=38, id=1014)
    chofer15 = Chofer(nombre="Alejandro Vargas", edad=41, id=1015)
    chofer16 = Chofer(nombre="Renata Castro", edad=37, id=1016)
    chofer17 = Chofer(nombre="Martín Herrera", edad=43, id=1017)
    chofer18 = Chofer(nombre="Lucía Rodríguez", edad=36, id=1018)
    chofer19 = Chofer(nombre="Juan Díaz", edad=44, id=1019)
    chofer20 = Chofer(nombre="Laura Pérez", edad=39, id=1020)

    # Crear 20 objetos Ruta
    fecha_base = datetime(2023, 11, 15, 8, 0, 0)  # Fecha base para las rutas

    ruta1 = Ruta(busAsociado=bus1, choferAsociado=chofer1, lugarInicio="Bogotá", lugarFin="Medellín", distancia=400, fechaSalida=fecha_base, fechaLlegada=fecha_base + timedelta(hours=8))
    rutas.append(ruta1)

    ruta2 = Ruta(busAsociado=bus2, choferAsociado=chofer2, lugarInicio="Medellín", lugarFin="Cali", distancia=300, fechaSalida=fecha_base + timedelta(days=1), fechaLlegada=fecha_base + timedelta(days=1, hours=6))
    rutas.append(ruta2)

    ruta3 = Ruta(busAsociado=bus3, choferAsociado=chofer3, lugarInicio="Cali", lugarFin="Pasto", distancia=250, fechaSalida=fecha_base + timedelta(days=2), fechaLlegada=fecha_base + timedelta(days=2, hours=5))
    rutas.append(ruta3)

    ruta4 = Ruta(busAsociado=bus4, choferAsociado=chofer4, lugarInicio="Pasto", lugarFin="Ipiales", distancia=80, fechaSalida=fecha_base + timedelta(days=3), fechaLlegada=fecha_base + timedelta(days=3, hours=2))
    rutas.append(ruta4)

    ruta5 = Ruta(busAsociado=bus5, choferAsociado=chofer5, lugarInicio="Ipiales", lugarFin="Popayán", distancia=200, fechaSalida=fecha_base + timedelta(days=4), fechaLlegada=fecha_base + timedelta(days=4, hours=4))
    rutas.append(ruta5)

    ruta6 = Ruta(busAsociado=bus6, choferAsociado=chofer6, lugarInicio="Popayán", lugarFin="Armenia", distancia=180, fechaSalida=fecha_base + timedelta(days=5), fechaLlegada=fecha_base + timedelta(days=5, hours=3))
    rutas.append(ruta6)

    ruta7 = Ruta(busAsociado=bus7, choferAsociado=chofer7, lugarInicio="Armenia", lugarFin="Pereira", distancia=50, fechaSalida=fecha_base + timedelta(days=6), fechaLlegada=fecha_base + timedelta(days=6, hours=1))
    rutas.append(ruta7)

    ruta8 = Ruta(busAsociado=bus8, choferAsociado=chofer8, lugarInicio="Pereira", lugarFin="Manizales", distancia=60, fechaSalida=fecha_base + timedelta(days=7), fechaLlegada=fecha_base + timedelta(days=7, hours=1, minutes=30))
    rutas.append(ruta8)

    ruta9 = Ruta(busAsociado=bus9, choferAsociado=chofer9, lugarInicio="Manizales", lugarFin="Honda", distancia=150, fechaSalida=fecha_base + timedelta(days=8), fechaLlegada=fecha_base + timedelta(days=8, hours=3))
    rutas.append(ruta9)

    ruta10 = Ruta(busAsociado=bus10, choferAsociado=chofer10, lugarInicio="Honda", lugarFin="Ibagué", distancia=120, fechaSalida=fecha_base + timedelta(days=9), fechaLlegada=fecha_base + timedelta(days=9, hours=2, minutes=30))
    rutas.append(ruta10)

    ruta11 = Ruta(busAsociado=bus11, choferAsociado=chofer11, lugarInicio="Ibagué", lugarFin="Neiva", distancia=180, fechaSalida=fecha_base + timedelta(days=10), fechaLlegada=fecha_base + timedelta(days=10, hours=3))
    rutas.append(ruta11)

    ruta12 = Ruta(busAsociado=bus12, choferAsociado=chofer12, lugarInicio="Neiva", lugarFin="Villavicencio", distancia=250, fechaSalida=fecha_base + timedelta(days=11), fechaLlegada=fecha_base + timedelta(days=11, hours=5))
    rutas.append(ruta12)

    ruta13 = Ruta(busAsociado=bus13, choferAsociado=chofer13, lugarInicio="Villavicencio", lugarFin="Yopal", distancia=200, fechaSalida=fecha_base + timedelta(days=12), fechaLlegada=fecha_base + timedelta(days=12, hours=4))
    rutas.append(ruta13)

    ruta14 = Ruta(busAsociado=bus14, choferAsociado=chofer14, lugarInicio="Yopal", lugarFin="Tunja", distancia=180, fechaSalida=fecha_base + timedelta(days=13), fechaLlegada=fecha_base + timedelta(days=13, hours=3, minutes=30))
    rutas.append(ruta14)

    ruta15 = Ruta(busAsociado=bus15, choferAsociado=chofer15, lugarInicio="Tunja", lugarFin="Bucaramanga", distancia=220, fechaSalida=fecha_base + timedelta(days=14), fechaLlegada=fecha_base + timedelta(days=14, hours=4, minutes=30))
    rutas.append(ruta15)

    ruta16 = Ruta(busAsociado=bus16, choferAsociado=chofer16, lugarInicio="Bucaramanga", lugarFin="Cúcuta", distancia=200, fechaSalida=fecha_base + timedelta(days=15), fechaLlegada=fecha_base + timedelta(days=15, hours=4))
    rutas.append(ruta16)

    ruta17 = Ruta(busAsociado=bus17, choferAsociado=chofer17, lugarInicio="Cúcuta", lugarFin="Valledupar", distancia=300, fechaSalida=fecha_base + timedelta(days=16), fechaLlegada=fecha_base + timedelta(days=16, hours=6))
    rutas.append(ruta17)

    ruta18 = Ruta(busAsociado=bus18, choferAsociado=chofer18, lugarInicio="Valledupar", lugarFin="Santa Marta", distancia=150, fechaSalida=fecha_base + timedelta(days=17), fechaLlegada=fecha_base + timedelta(days=17, hours=3))
    rutas.append(ruta18)

    ruta19 = Ruta(busAsociado=bus19, choferAsociado=chofer19, lugarInicio="Santa Marta", lugarFin="Barranquilla", distancia=90, fechaSalida=fecha_base + timedelta(days=18), fechaLlegada=fecha_base + timedelta(days=18, hours=2))
    rutas.append(ruta19)

    ruta20 = Ruta(busAsociado=bus20, choferAsociado=chofer20, lugarInicio="Barranquilla", lugarFin="Cartagena", distancia=120, fechaSalida=fecha_base + timedelta(days=19), fechaLlegada=fecha_base + timedelta(days=19, hours=2, minutes=30))
    rutas.append(ruta20)

    # Creando 4 objetos empresa.
    empresa1 = Empresa("RápidoOchoa", empleados = [chofer1, chofer2, chofer3],
                       rutas = [ruta1, ruta2, ruta3, ruta4, ruta5, ruta6],
                       buses = [bus1, bus2, bus3, bus4])
    empresa2 = Empresa("Bolivariano", empleados = [chofer4, chofer5, chofer6, chofer7, chofer8, chofer9, chofer10],
                       rutas = [ruta7, ruta8, ruta9, ruta10, ruta11, ruta12, ruta13],
                       buses = [bus5, bus6, bus7, bus8, bus9, bus10, bus11])
    empresa3 = Empresa("Brasilia", empleados = [chofer11, chofer12, chofer13, chofer14],
                       rutas = [ruta14, ruta15, ruta16, ruta17],
                       buses = [bus12, bus13, bus14, bus15, bus16])
    empresa4 = Empresa("Continental", empleados = [chofer15, chofer16, chofer17, chofer18, chofer19, chofer20],
                       rutas = [ruta18, ruta19, ruta20],
                       buses = [bus17, bus18, bus19, bus20])
    
    for empresa in Empresa.getEmpresas():
        for ruta in empresa.getRutas():
            empresa.asignarRuta(ruta)

    nombreArchivo = 'src/baseDatos/temp/Rutas.pkl'

    # Guardar datos
    guardar_datos(rutas, nombreArchivo)

    # Cargar datos
    datos_cargados = cargar_datos(nombreArchivo)

    if datos_cargados:
        print("Datos cargados:", datos_cargados)
    return datos_cargados

def LlamarBDPasajeros():
    import datetime as dt
    from Pasajero import Pasajero
    from Ruta import Ruta
    from Maleta import Maleta
    from Factura import Factura
    pasajeros = []

    # Crear objetos Maleta y Factura para usar en los Pasajeros
    maletas_pasajero1 = [Maleta(peso=20), Maleta(peso=10)]
    facturas_pasajero1 = [Factura(valor=100, fecha=dt.datetime(2023, 10, 26)), Factura(valor=50, fecha=dt.datetime(2023, 10, 27))]

    maletas_pasajero2 = [Maleta(peso=5)]
    facturas_pasajero2 = [Factura(valor=75, fecha=dt.datetime(2023, 10, 28))]

    # Crear objetos Pasajero para usar como acompañantes
    acompanante1 = Pasajero("Laura Gómez", 28, 1001)
    acompanante2 = Pasajero("Pedro Ramírez", 45, 1002)

    # Crear 20 objetos Pasajero
    pasajero1 = Pasajero("Juan Pérez", 35, 12345, maletas_pasajero1, 200, facturas_pasajero1, 2, acompanante1)
    pasajeros.append(pasajero1)

    pasajero2 = Pasajero("Ana López", 28, 54321, maletas_pasajero2, 150, facturas_pasajero2, 1, acompanante2)
    pasajeros.append(pasajero2)

    pasajero3 = Pasajero("Carlos Ruiz", 42, 67890, [], 300, [], 3, None)
    pasajeros.append(pasajero3)

    pasajero4 = Pasajero("María García", 31, 98765, [Maleta(peso=12)], 250, [Factura(valor=120, fecha=dt.datetime(2023, 10, 29))], 2, acompanante1)
    pasajeros.append(pasajero4)

    pasajero5 = Pasajero("Luis Martínez", 25, 13579, [Maleta(peso=25), Maleta(peso=8)], 180, [Factura(valor=90, fecha=dt.datetime(2023, 10, 30))], 1, acompanante2)
    pasajeros.append(pasajero5)

    pasajero6 = Pasajero("Sofía Díaz", 38, 24680, [], 350, [], 4, None)
    pasajeros.append(pasajero6)

    pasajero7 = Pasajero("Andrés Sánchez", 29, 11223, [Maleta(peso=7)], 220, [Factura(valor=80, fecha=dt.datetime(2023, 11, 1))], 2, acompanante1)
    pasajeros.append(pasajero7)

    pasajero8 = Pasajero("Valentina Torres", 47, 33445, [Maleta(peso=15)], 280, [Factura(valor=150, fecha=dt.datetime(2023, 11, 2))], 3, acompanante2)
    pasajeros.append(pasajero8)

    pasajero9 = Pasajero("Diego Ramírez", 33, 55667, [], 400, [], 1, None)
    pasajeros.append(pasajero9)

    pasajero10 = Pasajero("Isabella Vargas", 27, 77889, [Maleta(peso=30)], 200, [Factura(valor=110, fecha=dt.datetime(2023, 11, 3))], 2, acompanante1)
    pasajeros.append(pasajero10)

    pasajero11 = Pasajero("Mateo Castro", 40, 99001, [Maleta(peso=9)], 260, [Factura(valor=95, fecha=dt.datetime(2023, 11, 4))], 3, acompanante2)
    pasajeros.append(pasajero11)

    pasajero12 = Pasajero("Camila Herrera", 36, 11224, [], 320, [], 4, None)
    pasajeros.append(pasajero12)

    pasajero13 = Pasajero("Sebastián Rodríguez", 30, 22335, [Maleta(peso=18)], 230, [Factura(valor=130, fecha=dt.datetime(2023, 11, 5))], 1, acompanante1)
    pasajeros.append(pasajero13)

    pasajero14 = Pasajero("Daniela Jiménez", 43, 33446, [Maleta(peso=28), Maleta(peso=6)], 290, [Factura(valor=160, fecha=dt.datetime(2023, 11, 6))], 2, acompanante2)
    pasajeros.append(pasajero14)

    pasajero15 = Pasajero("Nicolás Silva", 26, 44557, [], 380, [], 3, None)
    pasajeros.append(pasajero15)

    pasajero16 = Pasajero("Gabriela Torres", 39, 55668, [Maleta(peso=11)], 210, [Factura(valor=100, fecha=dt.datetime(2023, 11, 7))], 4, acompanante1)
    pasajeros.append(pasajero16)

    pasajero17 = Pasajero("Alejandro Vargas", 32, 66779, [Maleta(peso=16)], 270, [Factura(valor=140, fecha=dt.datetime(2023, 11, 8))], 1, acompanante2)
    pasajeros.append(pasajero17)

    pasajero18 = Pasajero("Renata Castro", 46, 77880, [], 340, [], 2, None)
    pasajeros.append(pasajero18)

    pasajero19 = Pasajero("Martín Herrera", 28, 88991, [Maleta(peso=22)], 240, [Factura(valor=125, fecha=dt.datetime(2023, 11, 9))], 3, acompanante1)
    pasajeros.append(pasajero19)

    pasajero20 = Pasajero("Lucía Rodríguez", 37, 99002, [Maleta(peso=13)], 310, [Factura(valor=155, fecha=dt.datetime(2023, 11, 10))], 4, acompanante2)
    pasajeros.append(pasajero20)

    nombreArchivo = 'src/baseDatos/temp/Pasajeros.pkl'

    # Guardar datos
    guardar_datos(pasajeros, nombreArchivo)

    # Cargar datos
    datos_cargados = cargar_datos(nombreArchivo)

    if datos_cargados:
        print("Datos cargados:", datos_cargados)
    return datos_cargados