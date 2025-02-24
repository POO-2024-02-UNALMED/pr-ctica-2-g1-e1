import pickle
import datetime as dt
from Pasajero import Pasajero
from Ruta import Ruta
from Maleta import Maleta
from Factura import Factura
from Contabilidad import Contabilidad
from Bus import Bus
from Chofer import Chofer
from Empresa import Empresa
from Asiento import Asiento
from datetime import datetime, timedelta
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



def LlamarBD():
    rutas = []


    asiento1 = Asiento(None,True,"Perfecto Estado")
    asiento2 = Asiento(None,True,"Necesita Reparacion")
    asiento3 = Asiento(None,True,"Perfecto Estado")
    asientos1 = [asiento1,asiento2,asiento3]
    asiento4 = Asiento(None,True,"Perfecto Estado")
    asiento5 = Asiento(None,True,"Necesita Reparacion")
    asiento6 = Asiento(None,True,"En Mantenimiento")
    asientos2 = [asiento4,asiento5,asiento6]
    asiento7 = Asiento(None,True,"Perfecto Estado")
    asiento8 = Asiento(None,True,"Necesita Reparacion")
    asiento9 = Asiento(None,True,"En Mantenimiento")
    asientos3 = [asiento7,asiento8,asiento9]
    asiento10 = Asiento(None,True,"Perfecto Estado")
    asiento11 = Asiento(None,True,"Perfecto Estado")
    asiento12 = Asiento(None,True,"En Mantenimientoacion")
    asientos4 = [asiento10,asiento11,asiento12]
    asiento13 = Asiento(None,True,"Perfecto Estado")
    asiento14 = Asiento(None,True,"Perfecto Estado")
    asiento15 = Asiento(None,True,"Necesita Reparacion")
    asientos5 = [asiento13,asiento14,asiento15]
    asiento16 = Asiento(None,True,"En Mantenimiento")
    asiento17 = Asiento(None,True,"Perfecto Estado")
    asiento18 = Asiento(None,True,"Necesita Reparacion")
    asientos6 = [asiento16,asiento17,asiento18]
    asiento19 = Asiento(None,True,"En Mantenimiento")
    asiento20 = Asiento(None,True,"Perfecto Estado")
    asiento21 = Asiento(None,True,"Necesita Reparacion")
    asientos7 = [asiento19,asiento20,asiento21]
    asiento22 = Asiento(None,True,"En Mantenimiento")
    asiento23 = Asiento(None,False,"Perfecto Estado")
    asiento24 = Asiento(None,True,"NecesitaEn Mantenimiento")  
    asientos8 = [asiento22,asiento23,asiento24]
    asiento25 = Asiento(None,False,"Perfecto Estado")
    asiento26 = Asiento(None,True,"Necesita Reparacion")
    asiento27 = Asiento(None,False,"En Mantenimiento")
    asientos9 = [asiento25,asiento26,asiento27]
    asiento28 = Asiento(None,True,"Perfecto Estado")
    asiento29 = Asiento(None,True,"Necesita Reparacion")
    asiento30 = Asiento(None,False,"En Mantenimiento")
    asientos10 = [asiento28,asiento29,asiento30]
    asiento31 = Asiento(None,True,"Perfecto Estado")
    asiento32 = Asiento(None,True,"Necesita Reparacion")
    asiento33 = Asiento(None,False,"En Mantenimiento")
    asientos11 = [asiento31,asiento32,asiento33]
    asiento34 = Asiento(None,True,"Perfecto Estado")
    asiento35 = Asiento(None,True,"Necesita Reparacion")
    asiento36 = Asiento(None,False,"En Mantenimiento")
    asientos12 = [asiento34,asiento35,asiento36]
    asiento37 = Asiento(None,True,"Perfecto Estado")
    asiento38 = Asiento(None,False,"Necesita Reparacion")
    asiento39 = Asiento(None,True,"En Mantenimiento")
    asientos13 = [asiento37,asiento38,asiento39]
    asiento40 = Asiento(None,True,"Perfecto Estado")
    asiento41 = Asiento(None,False,"Necesita Reparacion")
    asiento42 = Asiento(None,True,"En Mantenimiento")
    asientos14 = [asiento40,asiento41,asiento42]
    asiento43 = Asiento(None,True,"Perfecto Estado")
    asiento44 = Asiento(None,True,"Necesita Reparacion")
    asiento45 = Asiento(None,False,"En Mantenimiento")
    asientos15 = [asiento43,asiento44,asiento45]
    asiento46 = Asiento(None,True,"Perfecto Estado")
    asiento47 = Asiento(None,False,"Perfecto Estado")
    asiento48 = Asiento(None,True,"En Mantenimiento")
    asientos16 = [asiento46,asiento47,asiento48]

    asiento49 = Asiento(None,True,"Perfecto Estado")
    asiento50 = Asiento(None,False,"Perfecto Estado")
    asiento51 = Asiento(None,True,"En Mantenimiento")

    asiento53 = Asiento(None,True,"Perfecto Estado")
    asiento54 = Asiento(None,False,"Perfecto Estado")
    asiento55 = Asiento(None,True,"En Mantenimiento")
    asientos18 = [asiento51,asiento53,asiento54]        
    asiento57 = Asiento(None,True,"Perfecto Estado")
    asiento58 = Asiento(None,False,"Perfecto Estado")
    asiento59 = Asiento(None,True,"En Mantenimiento")
    asientos19 = [asiento55,asiento57,asiento59]
    asiento61 = Asiento(None,True,"Perfecto Estado")
    asiento62 = Asiento(None,False,"Perfecto Estado")
    asiento63 = Asiento(None,True,"En Mantenimiento")
    asientos20 = [asiento61,asiento62,asiento63]
    asientos17 = [asiento49,asiento58,asiento50]


    # Crear objetos Bus
    bus1 = Bus(placa="ABC-123", cantidadAsientos=30,kilometrosRecorridos =1000, asientos = asientos1 ,consumo= 21.0,pesoMaximo=500, estado="Perfecto Estado")
    bus2 = Bus(placa="DEF-456", cantidadAsientos=40,kilometrosRecorridos =1052, asientos = asientos2 ,consumo= 22.0,pesoMaximo=750, estado="Necesita Reparación")
    bus3 = Bus(placa="GHI-789", cantidadAsientos=35,kilometrosRecorridos =1052, asientos = asientos3 ,consumo= 23.0,pesoMaximo=1000, estado="Perfecto Estado")
    bus4 = Bus(placa="JKL-012", cantidadAsientos=45, kilometrosRecorridos =1520,asientos = asientos4 ,consumo= 24.0,pesoMaximo=1250, estado="En Mantenimiento")
    bus5 = Bus(placa="MNO-345", cantidadAsientos=30, kilometrosRecorridos =1520,asientos = asientos5 ,consumo= 25.0,pesoMaximo=500, estado="Perfecto Estado")
    bus6 = Bus(placa="PQR-678", cantidadAsientos=40, kilometrosRecorridos =1052,asientos = asientos6 ,consumo= 26.0,pesoMaximo=750, estado="Necesita Reparación")
    bus7 = Bus(placa="STU-901", cantidadAsientos=35, kilometrosRecorridos =2000,asientos = asientos7 ,consumo= 27.0,pesoMaximo=1000, estado="Perfecto Estado")
    bus8 = Bus(placa="VWX-234", cantidadAsientos=45,kilometrosRecorridos =2000, asientos = asientos8 ,consumo= 28.0,pesoMaximo=1250, estado="En Mantenimiento")
    bus9 = Bus(placa="YZA-567", cantidadAsientos=30, kilometrosRecorridos =2000,asientos = asientos9 ,consumo= 29.0,pesoMaximo=500, estado="Perfecto Estado")
    bus10 = Bus(placa="BCD-890", cantidadAsientos=40,kilometrosRecorridos =1200,asientos = asientos10 ,consumo= 30.0, pesoMaximo=750, estado="Necesita Reparación")
    bus11 = Bus(placa="EFG-123", cantidadAsientos=35, kilometrosRecorridos =1200,asientos = asientos11 ,consumo= 31.0,pesoMaximo=1000, estado="Perfecto Estado")
    bus12 = Bus(placa="HIJ-456", cantidadAsientos=45,kilometrosRecorridos =3000,asientos = asientos12 ,consumo= 32.0,pesoMaximo=1250, estado="En Mantenimiento")
    bus13 = Bus(placa="KLM-789", cantidadAsientos=30,kilometrosRecorridos =3000,asientos = asientos13 ,consumo= 33.0, pesoMaximo=500, estado="Perfecto Estado")
    bus14 = Bus(placa="NOP-012", cantidadAsientos=40,kilometrosRecorridos =3000,asientos = asientos14 ,consumo= 34.0, pesoMaximo=750, estado="Necesita Reparación")
    bus15 = Bus(placa="QRS-345", cantidadAsientos=35,kilometrosRecorridos =3000,asientos = asientos15 ,consumo= 35.0, pesoMaximo=1000, estado="Perfecto Estado")
    bus16 = Bus(placa="TUV-678", cantidadAsientos=45,kilometrosRecorridos =3000,asientos = asientos16 ,consumo= 36.0,pesoMaximo=1250, estado="En Mantenimiento")
    bus17 = Bus(placa="WXY-901", cantidadAsientos=30,kilometrosRecorridos =1000,asientos = asientos17 ,consumo= 37.0, pesoMaximo=500, estado="Perfecto Estado")
    bus18 = Bus(placa="ZAB-234", cantidadAsientos=40,kilometrosRecorridos =1000,asientos = asientos18 ,consumo= 38.0, pesoMaximo=750, estado="Necesita Reparación")
    bus19 = Bus(placa="CDE-567", cantidadAsientos=35,kilometrosRecorridos =1000,asientos = asientos19 ,consumo= 39.0,pesoMaximo=1000, estado="Perfecto Estado")
    bus20 = Bus(placa="FGH-890", cantidadAsientos=45,kilometrosRecorridos =1000,asientos = asientos20 ,consumo= 40.0, pesoMaximo=1250, estado="En Mantenimiento")

    # Crear objetos Chofer
    chofer1 = Chofer(nombre="Carlos Pérez", edad=40, id=1001,bus=bus20)
    chofer2 = Chofer(nombre="Ana Gómez", edad=35, id=1002,bus=bus1)
    chofer3 = Chofer(nombre="Luis Martínez", edad=45, id=1003,bus=bus2)
    chofer4 = Chofer(nombre="Sofía Díaz", edad=38, id=1004,bus=bus3)
    chofer5 = Chofer(nombre="Andrés Sánchez", edad=42, id=1005,bus=bus4)
    chofer6 = Chofer(nombre="Valentina Torres", edad=39, id=1006,bus=bus5)
    chofer7 = Chofer(nombre="Diego Ramírez", edad=41, id=1007,bus=bus6)
    chofer8 = Chofer(nombre="Isabella Vargas", edad=37, id=1008,bus=bus7)
    chofer9 = Chofer(nombre="Mateo Castro", edad=43, id=1009,bus=bus8)
    chofer10 = Chofer(nombre="Camila Herrera", edad=36, id=1010,bus=bus9)
    chofer11 = Chofer(nombre="Sebastián Rodríguez", edad=44, id=1011,bus=bus10)
    chofer12 = Chofer(nombre="Daniela Jiménez", edad=39, id=1012,bus=bus11)
    chofer13 = Chofer(nombre="Nicolás Silva", edad=40, id=1013,bus=bus12)
    chofer14 = Chofer(nombre="Gabriela Torres", edad=38, id=1014,bus=bus13)
    chofer15 = Chofer(nombre="Alejandro Vargas", edad=41, id=1015,bus=bus14)
    chofer16 = Chofer(nombre="Renata Castro", edad=37, id=1016,bus=bus15)
    chofer17 = Chofer(nombre="Martín Herrera", edad=43, id=1017,bus=bus16)
    chofer18 = Chofer(nombre="Lucía Rodríguez", edad=36, id=1018,bus=bus17)
    chofer19 = Chofer(nombre="Juan Díaz", edad=44, id=1019,bus=bus18)
    chofer20 = Chofer(nombre="Laura Pérez", edad=39, id=1020,bus=bus19)

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

    buses= []
    choferes= []
    asientos =[]
    empresas = Empresa.getEmpresas()
    for ruta in rutas:
        buses.append(ruta.getBusAsociado())
        choferes.append(ruta.getChoferAsociado())

    for empresa in Empresa.getEmpresas():
        for ruta in empresa.getRutas():
            empresa.asignarRuta(ruta)
        for bus in empresa.getBuses():
            buses.append(bus)
            for asiento in bus.getAsientos():
                asientos.append(asiento)
                asiento.setBus(bus)




    pasajeros = []

    # Crear objetos Maleta y Factura para usar en los Pasajeros
    maletas_pasajero1 = [Maleta(peso=20), Maleta(peso=10)]
    
    facturas_pasajero1 = [Factura(nombreUsuario= "Juan Pérez",idUsuario = 12345 ,rutaElegida= ruta1,numAsientosAsignados = 1,valor=75,cantidadMaletas = 2, fecha=dt.datetime(2023, 10, 28))]
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

    facturas = []
    maletas= []

    for i in range(len(pasajeros)):

        pasajero=pasajeros[i]
        if pasajero.getMaletas():
            for maleta in pasajero.getMaletas():
                maletas.append(maleta)

        pasajeroFacturas =pasajero.getFacturas()
        for factura in pasajeroFacturas:
            facturas.append(factura)
        asientofor = asientos[i]


        asientofor.setUsuario(pasajero)
        asientofor.getBus().getEquipaje().extend(pasajero.getMaletas())

    nombreArchivo = 'src/baseDatos/temp/Pasajeros.pkl'
    nombreArchivoFactura= 'src/baseDatos/temp/Facturas.pkl'
    nombreArchivoContabilidad = 'src/baseDatos/temp/Contabilidad.pkl'
    nombreArchivoRutas = 'src/baseDatos/temp/Rutas.pkl'
    nombreArchivoBus= 'src/baseDatos/temp/Bus.pkl'
    nombreArchivoChofer= 'src/baseDatos/temp/Chofer.pkl'
    nombreArchivoEmpresa = 'src/baseDatos/temp/Empresa.pkl'
    nombreArchivoAsientos= 'src/baseDatos/temp/Asientos.pkl'
    nombreArchivoMaletas= 'src/baseDatos/temp/Maletas.pkl'
    
    Contabilidad1 = Contabilidad(100000000,50000000, facturas,[])# la lista son las facturas reembolsadas (no hay)
    # Guardar datos 
    guardar_datos(rutas, nombreArchivoRutas)
    guardar_datos(buses, nombreArchivoBus)
    guardar_datos(choferes, nombreArchivoChofer)
    guardar_datos(empresas, nombreArchivoEmpresa)
    guardar_datos(pasajeros, nombreArchivo)
    guardar_datos(facturas, nombreArchivoFactura)
    guardar_datos(Contabilidad1,nombreArchivoContabilidad)
    guardar_datos(asientos,nombreArchivoAsientos)
    guardar_datos(maletas,nombreArchivoMaletas)
    # Cargar datos
    datos_Pasajeros = cargar_datos(nombreArchivo)
    datos_Facturas = cargar_datos(nombreArchivoFactura)
    datos_Contabilidad = cargar_datos(nombreArchivoContabilidad)
    datos_cargado_Rutas = cargar_datos(nombreArchivoRutas)
    datos_cargados_Bus = cargar_datos(nombreArchivoBus)
    datos_cargados_Chofer = cargar_datos(nombreArchivoChofer)
    datos_cargados_Empresa = cargar_datos(nombreArchivoEmpresa)
    datos_cargados_Asientos = cargar_datos(nombreArchivoAsientos) 
    datos_cargados_Maletas = cargar_datos(nombreArchivoMaletas)   
    return datos_Pasajeros, datos_Facturas, datos_Contabilidad, datos_cargado_Rutas, datos_cargados_Bus , datos_cargados_Chofer, datos_cargados_Empresa,datos_cargados_Asientos, datos_cargados_Maletas
