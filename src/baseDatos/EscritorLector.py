import pickle

def guardar_datos(datos, nombreArchivo):
    """

    Guarda los datos en un archivo utilizando pickle.

    Argumentoss:

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
Pasajeros = {
    'nombre': 'Ejemplo',
    'edad': 30,
    'lista': [1, 2, 3]
}

nombreArchivo = 'src/baseDatos/temp/Pasajeros.pkl'

# Guardar datos
guardar_datos(Pasajeros, nombreArchivo)

# Cargar datos
datos_cargados = cargar_datos(nombreArchivo)

if datos_cargados:
    print("Datos cargados:", datos_cargados)