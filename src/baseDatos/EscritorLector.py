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
    from datetime import datetime, timedelta

    rutas = []

    # Crear objetos Bus
    bus1 = Bus(placa="ABC-123", cantidadAsientos=30, pesoMaximo=500.0, estado="Perfecto Estado")
    bus2 = Bus(placa="DEF-456", cantidadAsientos=40, pesoMaximo=750.0, estado="Necesita Reparación")
    bus3 = Bus(placa="GHI-789", cantidadAsientos=35, pesoMaximo=1000.0, estado="Perfecto Estado")
    bus4 = Bus(placa="JKL-012", cantidadAsientos=45, pesoMaximo=1250.0, estado="En Mantenimiento")
    bus5 = Bus(placa="MNO-345", cantidadAsientos=30, pesoMaximo=500.0, estado="Perfecto Estado")
    bus6 = Bus(placa="PQR-678", cantidadAsientos=40, pesoMaximo=750.0, estado="Necesita Reparación")
    bus7 = Bus(placa="STU-901", cantidadAsientos=35, pesoMaximo=1000.0, estado="Perfecto Estado")
    bus8 = Bus(placa="VWX-234", cantidadAsientos=45, pesoMaximo=1250.0, estado="En Mantenimiento")
    bus9 = Bus(placa="YZA-567", cantidadAsientos=30, pesoMaximo=500.0, estado="Perfecto Estado")
    bus10 = Bus(placa="BCD-890", cantidadAsientos=40, pesoMaximo=750.0, estado="Necesita Reparación")
    bus11 = Bus(placa="EFG-123", cantidadAsientos=35, pesoMaximo=1000.0, estado="Perfecto Estado")
    bus12 = Bus(placa="HIJ-456", cantidadAsientos=45, pesoMaximo=1250.0, estado="En Mantenimiento")
    bus13 = Bus(placa="KLM-789", cantidadAsientos=30, pesoMaximo=500.0, estado="Perfecto Estado")
    bus14 = Bus(placa="NOP-012", cantidadAsientos=40, pesoMaximo=750.0, estado="Necesita Reparación")
    bus15 = Bus(placa="QRS-345", cantidadAsientos=35, pesoMaximo=1000.0, estado="Perfecto Estado")
    bus16 = Bus(placa="TUV-678", cantidadAsientos=45, pesoMaximo=1250.0, estado="En Mantenimiento")
    bus17 = Bus(placa="WXY-901", cantidadAsientos=30, pesoMaximo=500.0, estado="Perfecto Estado")
    bus18 = Bus(placa="ZAB-234", cantidadAsientos=40, pesoMaximo=750.0, estado="Necesita Reparación")
    bus19 = Bus(placa="CDE-567", cantidadAsientos=35, pesoMaximo=1000.0, estado="Perfecto Estado")
    bus20 = Bus(placa="FGH-890", cantidadAsientos=45, pesoMaximo=1250.0, estado="En Mantenimiento")

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

    ruta1 = Ruta(busAsociado=bus1, choferAsociado=chofer1, lugarInicio="Bogotá", lugarFin="Medellín", distancia=400.0, fechaSalida=fecha_base, fechaLlegada=fecha_base + timedelta(hours=8))
    rutas.append(ruta1)

    ruta2 = Ruta(busAsociado=bus2, choferAsociado=chofer2, lugarInicio="Medellín", lugarFin="Cali", distancia=300.0, fechaSalida=fecha_base + timedelta(days=1), fechaLlegada=fecha_base + timedelta(days=1, hours=6))
    rutas.append(ruta2)

    ruta3 = Ruta(busAsociado=bus3, choferAsociado=chofer3, lugarInicio="Cali", lugarFin="Pasto", distancia=250.0, fechaSalida=fecha_base + timedelta(days=2), fechaLlegada=fecha_base + timedelta(days=2, hours=5))
    rutas.append(ruta3)

    ruta4 = Ruta(busAsociado=bus4, choferAsociado=chofer4, lugarInicio="Pasto", lugarFin="Ipiales", distancia=80.0, fechaSalida=fecha_base + timedelta(days=3), fechaLlegada=fecha_base + timedelta(days=3, hours=2))
    rutas.append(ruta4)

    ruta5 = Ruta(busAsociado=bus5, choferAsociado=chofer5, lugarInicio="Ipiales", lugarFin="Popayán", distancia=200.0, fechaSalida=fecha_base + timedelta(days=4), fechaLlegada=fecha_base + timedelta(days=4, hours=4))
    rutas.append(ruta5)

    ruta6 = Ruta(busAsociado=bus6, choferAsociado=chofer6, lugarInicio="Popayán", lugarFin="Armenia", distancia=180.0, fechaSalida=fecha_base + timedelta(days=5), fechaLlegada=fecha_base + timedelta(days=5, hours=3))
    rutas.append(ruta6)

    ruta7 = Ruta(busAsociado=bus7, choferAsociado=chofer7, lugarInicio="Armenia", lugarFin="Pereira", distancia=50.0, fechaSalida=fecha_base + timedelta(days=6), fechaLlegada=fecha_base + timedelta(days=6, hours=1))
    rutas.append(ruta7)

    ruta8 = Ruta(busAsociado=bus8, choferAsociado=chofer8, lugarInicio="Pereira", lugarFin="Manizales", distancia=60.0, fechaSalida=fecha_base + timedelta(days=7), fechaLlegada=fecha_base + timedelta(days=7, hours=1, minutes=30))
    rutas.append(ruta8)

    ruta9 = Ruta(busAsociado=bus9, choferAsociado=chofer9, lugarInicio="Manizales", lugarFin="Honda", distancia=150.0, fechaSalida=fecha_base + timedelta(days=8), fechaLlegada=fecha_base + timedelta(days=8, hours=3))
    rutas.append(ruta9)

    ruta10 = Ruta(busAsociado=bus10, choferAsociado=chofer10, lugarInicio="Honda", lugarFin="Ibagué", distancia=120.0, fechaSalida=fecha_base + timedelta(days=9), fechaLlegada=fecha_base + timedelta(days=9, hours=2, minutes=30))
    rutas.append(ruta10)

    ruta11 = Ruta(busAsociado=bus11, choferAsociado=chofer11, lugarInicio="Ibagué", lugarFin="Neiva", distancia=180.0, fechaSalida=fecha_base + timedelta(days=10), fechaLlegada=fecha_base + timedelta(days=10, hours=3))
    rutas.append(ruta11)

    ruta12 = Ruta(busAsociado=bus12, choferAsociado=chofer12, lugarInicio="Neiva", lugarFin="Villavicencio", distancia=250.0, fechaSalida=fecha_base + timedelta(days=11), fechaLlegada=fecha_base + timedelta(days=11, hours=5))
    rutas.append(ruta12)

    ruta13 = Ruta(busAsociado=bus13, choferAsociado=chofer13, lugarInicio="Villavicencio", lugarFin="Yopal", distancia=200.0, fechaSalida=fecha_base + timedelta(days=12), fechaLlegada=fecha_base + timedelta(days=12, hours=4))
    rutas.append(ruta13)

    ruta14 = Ruta(busAsociado=bus14, choferAsociado=chofer14, lugarInicio="Yopal", lugarFin="Tunja", distancia=180.0, fechaSalida=fecha_base + timedelta(days=13), fechaLlegada=fecha_base + timedelta(days=13, hours=3, minutes=30))
    rutas.append(ruta14)

    ruta15 = Ruta(busAsociado=bus15, choferAsociado=chofer15, lugarInicio="Tunja", lugarFin="Bucaramanga", distancia=220.0, fechaSalida=fecha_base + timedelta(days=14), fechaLlegada=fecha_base + timedelta(days=14, hours=4, minutes=30))
    rutas.append(ruta15)

    ruta16 = Ruta(busAsociado=bus16, choferAsociado=chofer16, lugarInicio="Bucaramanga", lugarFin="Cúcuta", distancia=200.0, fechaSalida=fecha_base + timedelta(days=15), fechaLlegada=fecha_base + timedelta(days=15, hours=4))
    rutas.append(ruta16)

    ruta17 = Ruta(busAsociado=bus17, choferAsociado=chofer17, lugarInicio="Cúcuta", lugarFin="Valledupar", distancia=300.0, fechaSalida=fecha_base + timedelta(days=16), fechaLlegada=fecha_base + timedelta(days=16, hours=6))
    rutas.append(ruta17)

    ruta18 = Ruta(busAsociado=bus18, choferAsociado=chofer18, lugarInicio="Valledupar", lugarFin="Santa Marta", distancia=150.0, fechaSalida=fecha_base + timedelta(days=17), fechaLlegada=fecha_base + timedelta(days=17, hours=3))
    rutas.append(ruta18)

    ruta19 = Ruta(busAsociado=bus19, choferAsociado=chofer19, lugarInicio="Santa Marta", lugarFin="Barranquilla", distancia=90.0, fechaSalida=fecha_base + timedelta(days=18), fechaLlegada=fecha_base + timedelta(days=18, hours=2))
    rutas.append(ruta19)

    ruta20 = Ruta(busAsociado=bus20, choferAsociado=chofer20, lugarInicio="Barranquilla", lugarFin="Cartagena", distancia=120.0, fechaSalida=fecha_base + timedelta(days=19), fechaLlegada=fecha_base + timedelta(days=19, hours=2, minutes=30))
    rutas.append(ruta20)

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
    maletas_pasajero1 = [Maleta(peso=20.0), Maleta(peso=10.0)]
    facturas_pasajero1 = [Factura(valor=100.0, fecha=dt.datetime(2023, 10, 26)), Factura(valor=50.0, fecha=dt.datetime(2023, 10, 27))]

    maletas_pasajero2 = [Maleta(peso=5.0)]
    facturas_pasajero2 = [Factura(valor=75.0, fecha=dt.datetime(2023, 10, 28))]

    # Crear objetos Pasajero para usar como acompañantes
    acompanante1 = Pasajero("Laura Gómez", 28, 1001)
    acompanante2 = Pasajero("Pedro Ramírez", 45, 1002)

    # Crear 20 objetos Pasajero
    pasajero1 = Pasajero("Juan Pérez", 35, 12345, maletas_pasajero1, 200.0, facturas_pasajero1, 2, acompanante1)
    pasajeros.append(pasajero1)

    pasajero2 = Pasajero("Ana López", 28, 54321, maletas_pasajero2, 150.0, facturas_pasajero2, 1, acompanante2)
    pasajeros.append(pasajero2)

    pasajero3 = Pasajero("Carlos Ruiz", 42, 67890, [], 300.0, [], 3, None)
    pasajeros.append(pasajero3)

    pasajero4 = Pasajero("María García", 31, 98765, [Maleta(peso=12.0)], 250.0, [Factura(valor=120.0, fecha=dt.datetime(2023, 10, 29))], 2, acompanante1)
    pasajeros.append(pasajero4)

    pasajero5 = Pasajero("Luis Martínez", 25, 13579, [Maleta(peso=25.0), Maleta(peso=8.0)], 180.0, [Factura(valor=90.0, fecha=dt.datetime(2023, 10, 30))], 1, acompanante2)
    pasajeros.append(pasajero5)

    pasajero6 = Pasajero("Sofía Díaz", 38, 24680, [], 350.0, [], 4, None)
    pasajeros.append(pasajero6)

    pasajero7 = Pasajero("Andrés Sánchez", 29, 11223, [Maleta(peso=7.0)], 220.0, [Factura(valor=80.0, fecha=dt.datetime(2023, 11, 1))], 2, acompanante1)
    pasajeros.append(pasajero7)

    pasajero8 = Pasajero("Valentina Torres", 47, 33445, [Maleta(peso=15.0)], 280.0, [Factura(valor=150.0, fecha=dt.datetime(2023, 11, 2))], 3, acompanante2)
    pasajeros.append(pasajero8)

    pasajero9 = Pasajero("Diego Ramírez", 33, 55667, [], 400.0, [], 1, None)
    pasajeros.append(pasajero9)

    pasajero10 = Pasajero("Isabella Vargas", 27, 77889, [Maleta(peso=30.0)], 200.0, [Factura(valor=110.0, fecha=dt.datetime(2023, 11, 3))], 2, acompanante1)
    pasajeros.append(pasajero10)

    pasajero11 = Pasajero("Mateo Castro", 40, 99001, [Maleta(peso=9.0)], 260.0, [Factura(valor=95.0, fecha=dt.datetime(2023, 11, 4))], 3, acompanante2)
    pasajeros.append(pasajero11)

    pasajero12 = Pasajero("Camila Herrera", 36, 11224, [], 320.0, [], 4, None)
    pasajeros.append(pasajero12)

    pasajero13 = Pasajero("Sebastián Rodríguez", 30, 22335, [Maleta(peso=18.0)], 230.0, [Factura(valor=130.0, fecha=dt.datetime(2023, 11, 5))], 1, acompanante1)
    pasajeros.append(pasajero13)

    pasajero14 = Pasajero("Daniela Jiménez", 43, 33446, [Maleta(peso=28.0), Maleta(peso=6.0)], 290.0, [Factura(valor=160.0, fecha=dt.datetime(2023, 11, 6))], 2, acompanante2)
    pasajeros.append(pasajero14)

    pasajero15 = Pasajero("Nicolás Silva", 26, 44557, [], 380.0, [], 3, None)
    pasajeros.append(pasajero15)

    pasajero16 = Pasajero("Gabriela Torres", 39, 55668, [Maleta(peso=11.0)], 210.0, [Factura(valor=100.0, fecha=dt.datetime(2023, 11, 7))], 4, acompanante1)
    pasajeros.append(pasajero16)

    pasajero17 = Pasajero("Alejandro Vargas", 32, 66779, [Maleta(peso=16.0)], 270.0, [Factura(valor=140.0, fecha=dt.datetime(2023, 11, 8))], 1, acompanante2)
    pasajeros.append(pasajero17)

    pasajero18 = Pasajero("Renata Castro", 46, 77880, [], 340.0, [], 2, None)
    pasajeros.append(pasajero18)

    pasajero19 = Pasajero("Martín Herrera", 28, 88991, [Maleta(peso=22.0)], 240.0, [Factura(valor=125.0, fecha=dt.datetime(2023, 11, 9))], 3, acompanante1)
    pasajeros.append(pasajero19)

    pasajero20 = Pasajero("Lucía Rodríguez", 37, 99002, [Maleta(peso=13.0)], 310.0, [Factura(valor=155.0, fecha=dt.datetime(2023, 11, 10))], 4, acompanante2)
    pasajeros.append(pasajero20)

    nombreArchivo = 'src/baseDatos/temp/Pasajeros.pkl'

    # Guardar datos
    guardar_datos(pasajeros, nombreArchivo)

    # Cargar datos
    datos_cargados = cargar_datos(nombreArchivo)

    if datos_cargados:
        print("Datos cargados:", datos_cargados)
    return datos_cargados