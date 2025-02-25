import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
import FieldFrame as FF
import VentanaInicio as VI
import datetime

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.title("Sistema - Ventana Principal")
        self.geometry(f"{screenWidth}x{screenHeight}")
        self.configurarMenu()
        self.crearWidgets()
        self.horaZero= datetime.datetime.now()
    
    def configurarMenu(self):
        menuBar = Menu(self, font="Arial")

        menuArchivo = Menu(menuBar, tearoff=0)
        menuArchivo.add_command(label="Aplicación", command=self.mostrarInfo)
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=self.cerrarSesion)

        menuProcesos = Menu(menuBar, tearoff=0)
        #menuProcesos.add_command(label="Funcionalidad 1")
        #menuProcesos.add_command(label="Funcionalidad 2")
        menuProcesos.add_command(label="Funcionalidad 3", command=self.mostrarReembolsos)
        menuProcesos.add_command(label = "Funcionalidad 4", command = self.creacionRuta)
        
        menuAyuda = Menu(menuBar, tearoff=0)
        menuAyuda.add_command(label="Acerca de", command=self.mostrarAutores)
        
        menuBar.add_cascade(label="Archivo", menu=menuArchivo)
        menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesos)
        menuBar.add_cascade(label="Ayuda", menu=menuAyuda)

        self.config(menu=menuBar)

    def crearWidgets(self):
        self.frameContenido = tk.Frame(self, bg="#3B1C32", bd=2, relief="solid")
        self.frameContenido.pack(expand=True, fill="both", padx=10, pady=10)
        tk.Label(
        self.frameContenido, 
        text="Seleccione una funcionalidad en el menú 'Procesos y Consultas' para comenzar.", 
        font=("Arial", 14), 
        wraplength=500, 
        bg="#3B1C32", 
        fg="white",
        justify="center"
       ).pack(expand=True, padx=20, pady=20)
    def mostrarReembolsos(self):

        for widget in self.frameContenido.winfo_children():
            widget.destroy()
        FrPrincipal= tk.Frame(self.frameContenido,bg="#3B1C32")
        tk.Label(FrPrincipal, text="Bienvenido al Sistema de Reembolsos de Tickets", bg="#A64D79",fg="white",
                 font=("Arial", 16)).pack(side=tk.TOP,pady=10)
        frame_forms = tk.Frame(FrPrincipal, bg="#6A1E55")
        frame_forms.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_respuestas = tk.Frame(FrPrincipal, bg="#A64D79")
        frame_respuestas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        criterios = ["Nombre en factura", "Número de documento", "Número de factura", "Número de maletas"]
        formulario = FF.FieldFrame(frame_forms, "Criterio", criterios, "Valor", bg="#A64D79")

        def analizarParametros(Parametros):
            ordenEsperado1 = ["Nombre en factura", "Número de documento", "Número de factura", "Número de maletas"]
            ordenActual = [campo for campo, entry in formulario.entries.items()]  # Obtén los nombres de los campos en el orden actual

            if ordenActual == ordenEsperado1:
                validacionReembolso(Parametros)

        def validacionReembolso(parametros):
            """
            Valida los reembolsos buscando al pasajero por nombre y número de documento.

            """

            from Pasajero import Pasajero
            from Excepciones import InexistenciaExcepcion, CampoFaltanteEx, ErrorTipoDatoEx
            from Persona import Persona
            from Contabilidad import Contabilidad
            nombrePasajero = None
            numeroDocumento = None
            numeroFactura = None
            for campo, valor in parametros:
                if campo == "Nombre en factura":
                    nombrePasajero = valor

                elif campo == "Número de documento":
                    numeroDocumento = valor

                    
                elif campo == "Número de factura":
                    numeroFactura = valor

                elif campo == "Número de maletas":
                    numeroMaletas = valor
            try:
                if nombrePasajero and numeroDocumento:
                    pasajero1 = Pasajero.buscarPasajero(nombrePasajero, numeroDocumento)

                    if pasajero1:

                        respuestas= pasajero1.solicitarReembolso(numeroDocumento,numeroFactura,self.horaZero)
                        mensaje_reembolso = respuestas[0]
                        mensaje_reembolso = respuestas[0]
                        tk.Label(frame_respuestas, text=mensaje_reembolso, bg="#6A1E55",fg="white").pack(pady=10)
                        if respuestas and len(respuestas) == 2:  # Verifica si la respuesta tiene 2 elementos
                            facturaUser= respuestas[1]
                            nums_maletas=[]
                            mensaje_2 = facturaUser.verificarBusAsociado()
                            tk.Label(frame_respuestas, text=mensaje_2, bg="#6A1E55",fg="white").pack(pady=10)
                            if "Existe un Bus Asociado a la ruta de la factura" in mensaje_2:
                                # Mostrar el mensaje en el frameContenido  
                                mensaje_3 = facturaUser.verificarRutaAsociada()
                                tk.Label(frame_respuestas, text=mensaje_3, bg="#6A1E55",fg="white").pack(pady=10)
                                
                                if "El asiento liberado puede ser reservado nuevament" in mensaje_3:

                                    def validarMaletas():
                                        from Excepciones.CampoFaltanteEx import CampoFaltanteEx
                                        a = 0
                                        total_maletas = int(numeroMaletas)
                                        maletas_verificadas = []  # Lista de identificadores de maletas válidas

                                        while a < total_maletas:
                                            try:
                                                entry_maleta = formulario2.entries[f"Maleta {a+1}"]  # Recupera el campo correcto
                                                IdMaletaUser = entry_maleta.get().strip()

                                                if not IdMaletaUser:
                                                    raise CampoFaltanteEx("Número de maleta")

                                                IdMaletaUser = int(IdMaletaUser)  # Asegurar que es un número entero
                                                verificacion = facturaUser.verificarMaletaBusAsociado(IdMaletaUser)

                                                if verificacion:
                                                    maletas_verificadas.append(IdMaletaUser)
                                                    tk.Label(frame_respuestas, text=f"La maleta con número {IdMaletaUser} está en el bus de la factura",
                                                            bg="#6A1E55", fg="white").pack(pady=10)
                                                    a += 1  # Solo avanzar si la maleta es válida

                                                else:
                                                    respuesta = messagebox.askyesno("Maleta no encontrada", "¿Desea volver a ingresar el identificador de la maleta?")
                                                    if not respuesta:
                                                        a += 1  # Solo avanzar si el usuario no quiere reingresar
                                                    else:
                                                        return

                                            except KeyError:
                                                messagebox.showerror("Error", f"No se encontró la entrada 'Maleta {a+1}' en el formulario.")
                                                return
                                            except ValueError:
                                                messagebox.showerror("Error de formato", "El número de maleta debe ser un número entero.")
                                                return
                                            except CampoFaltanteEx as e:
                                                e.mostrar_advertencia()
                                                return

                                        # Verificar que se obtuvieron todas las maletas antes de hacer el reembolso
                                        if len(maletas_verificadas) == total_maletas:
                                            mensaje_4 = facturaUser.eliminarMaletaBusAsociado(maletas_verificadas)
                                            tk.Label(frame_respuestas, text=mensaje_4, bg="#6A1E55", fg="white").pack(pady=10)

                                            if "ha sido eliminada del equipaje del bus" in mensaje_4: 
                                                pasajero1.setFacturas([])
                                                for widget in frame_respuestas.winfo_children():
                                                    widget.destroy()
                                                tk.Label(frame_respuestas, text="¡Reembolso exitoso! Su factura ha sido invalidada y el monto ha sido acreditado a su cuenta.", 
                                                        bg="#6A1E55", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
                                                tk.Label(frame_respuestas, text=Contabilidad.generarDesglose(facturaUser), 
                                                        bg="#6A1E55", fg="white").pack(pady=10)
                                                tk.Label(frame_respuestas, text=f"El monto reembolsado es: ${Contabilidad.montoReembolso(facturaUser)}", 
                                                        bg="#6A1E55", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
                                                tk.Label(frame_respuestas, text=f"Su nuevo saldo en wallet es: ${pasajero1.getWallet()}",
                                                        bg="#6A1E55", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

                                    btnAceptar.config(command= validarMaletas)
                                    btnAceptar.pack(side="bottom")
                                    btnBorrar.pack(side="bottom")
                                    criterios_maletas = [f"Maleta {i+1}" for i in range(int(numeroMaletas))]
                                    formulario2 = FF.FieldFrame(frame_forms, "Criterio", criterios_maletas, "Valor", bg="#A64D79")
                                    formulario2.pack(pady=10, padx=10, expand=False, fill="both")
                                else:
                                    pasajero1.revertirPasajes()
                            mensaje = facturaUser.eliminarMaletaBusAsociado(nums_maletas) 
                            if "No se pudo hacer el reembolso, La maleta con el numero de identificacion" in mensaje :
                                pasajero1.revertirPasajes()          

                    else:
                        raise InexistenciaExcepcion.InexistenciaExcepcion("Pasajero en el sistema")
                else:
                    raise CampoFaltanteEx.CampoFaltanteEx(campo)
            except InexistenciaExcepcion.InexistenciaExcepcion as e:
                e.mostrar_advertencia()
                return
            except CampoFaltanteEx.CampoFaltanteEx as e:
                e.mostrar_advertencia()
                return


        def borrarCampos():
            """Limpia los campos del formulario."""
            formulario.limpiarCampos()

        def obtenerParametros():
            """Recopila los parámetros del formulario, valida los tipos y los almacena en una lista."""
            parametros = []
            from Excepciones import CampoFaltanteEx, ErrorTipoDatoEx
            for campo, entry in formulario.entries.items():
                valor = entry.get()
                try:
                    if not valor:
                        raise CampoFaltanteEx.CampoFaltanteEx(campo)  # Lanza la excepción con el campo
                    else:
                        if campo == "Nombre en factura":
                            if not isinstance(valor, str):
                                raise ErrorTipoDatoEx(campo, str)
                        elif campo == "Número de documento":
                            try:
                                int(valor)  # Intenta convertir a entero
                            except ValueError:
                                raise ErrorTipoDatoEx.ErrorTipoDatoEx(campo, int)
                        elif campo == "Número de factura":
                            try:
                                int(valor)
                            except ValueError:
                                raise ErrorTipoDatoEx.ErrorTipoDatoEx(campo, int)
                        elif campo == "Número de maletas":
                            try:
                                int(valor)
                            except ValueError:
                                raise ErrorTipoDatoEx.ErrorTipoDatoEx(campo, int)
            
                    parametros.append((campo, valor))

                except CampoFaltanteEx.CampoFaltanteEx as e:
                    e.mostrar_advertencia()  # Muestra la advertencia usando el método de la excepción
                    return  # Sale de la función
                except ErrorTipoDatoEx.ErrorTipoDatoEx as e:
                    e.mostrar_advertencia()
                    return
            messagebox.showinfo("Proceso", "Su validación está en proceso.")
            analizarParametros(parametros)

        FrPrincipal.pack(pady=10, padx=10, expand=True, fill="both")
        formulario.pack(pady=10, padx=10, expand=False, fill="both")

        frame_botones = tk.Frame(frame_forms, bg="")
        frame_botones.pack(side="bottom", pady=20)  # Centra verticalmente el frame contenedor

        btnAceptar = tk.Button(frame_botones, text="Aceptar", command=obtenerParametros,bg="lightgray")
        btnAceptar.pack(side=tk.LEFT, padx=10)

        btnBorrar = tk.Button(frame_botones, text="Borrar", command=borrarCampos, bg="lightgray")
        btnBorrar.pack(side=tk.LEFT, padx=10) 

    def mostrarInfo(self):
        messagebox.showinfo("Información", "El proyecto se centra en crear una herramienta con la cual se establezca una comunicación entre los usuarios de una terminal de buses y las empresas de dicha terminal de manera que se sistematice los procesos más comunes que involucran a ambos.")
    
    def mostrarAutores(self):
        messagebox.showinfo("Autores", "Desarrollado por un equipo de desarrolladores integrado por. Salcedo Rodriguez Santiago Abelardo  , Cardona Ramirez Luis Mario, Rincon Stiven Brandon, Ceron Quintero David Fernando, Moreano Urresty Juan Camilo.")
    
    def cerrarSesion(self):
        self.destroy()
        VI.VentanaInicio()

    @staticmethod
    def verificacionExistencia(conjunto: list, busqueda) -> "InexistenciaExcepcion":
        """
        Se busca la existencia de un elemento en un conjunto.

        Parámetros:
            - conjunto: list[Object],
                Conjunto donde se hará la búsqueda.
            - busqueda:
                Elemento a buscar en el conjunto.

        Retorna:
            - existencia: bool.
                ¿Existe el elemento en el conjunto?. En caso de no existir,
                se genera un InexistenciaEception error.
        """

        from InexistenciaExcepcion import InexistenciaExcepcion

        # Realizando la búsqueda.
        for elemento in conjunto:
            if elemento == busqueda:
                return None
        else:
            return InexistenciaExcepcion("No existe el objeto buscado en la lista.")

    def ajustarParadas(self, empresa: "Empresa", trayecto: list[int], numeroParadas: int, factor: float, texto: tk.Text) -> list[int]:
        """
        Calcula el trayecto con parada origen -> parada destino, tal que
        se cumple (Si se puede) el número de paradas deseadas y un factor de crecimiento
        (Medido con base a la ruta óptima dada por el algoritmo de Bellman-Ford).

        Parámetros:
            - empresa: Empresa,
                Empresa a la cual se le hallará la ruta.
            - numeroParadas: int,
                Cantidad de paradas que se quiere tenga la ruta.
            - factor: float,
                Indica la cantidad máxima de expansión permitida en la ruta.
            - texto: Tk.Text,
                El encargado de mostrar el proceso.

        Retorna:
            - paradasReales: list[int],
                Ordinales de las paradas en el trayecto que cumplen
                (En la medida de lo posible) los requisitos.
        """

        from Red import Red

        if factor < 1:
            texto.insert("end", "Como el factor es menor a 1, el trayecto se va a quedar igual.")
            return None

        # Iniciando las variables necesarias.
        promedios = empresa.flujoPromedio()

        # Ajustando para que se tenga la cantidad de paradas deseada.
        numeroParadasCreadas = len(trayecto)
        paradasReales = [0 for _ in range(numeroParadas)]
        if numeroParadasCreadas > numeroParadas:
            texto.insert("end", "Como se necesita reducir el número de paradas, " +
                                "se va a calcular cuántas personas se bajan en la " +
                                "parada desde el origen, y se van a ir quitando en" +
                                " orden descendente de estos valores.\n")
        
            # Se buscará una ruta que maximice la cantidad de personas que usarán la ruta.
            salientes = [(0, 0) for _ in range(numeroParadasCreadas - 2)]
            for i in range(numeroParadasCreadas - 2):
                ordinalActual = trayecto[i + 1]
                salientes[i] = (i + 1, promedios[trayecto[0]][ordinalActual])

            # Hallando el orden de la cantidad de personas que se bajan en esa parada.
            concurrencia = sorted(salientes, key = lambda x: x[1], reverse = True)

            # Mostrando las paradas en orden de cantidad de salida.
            for i in range(len(concurrencia)):
                texto.insert("end", Red.Parada(trayecto[concurrencia[i][0]]) +
                                    " tiene " + str(salientes[concurrencia[i]][1]) +
                                    " personas saliendo en promedio desde " +
                                    Red.Parada(trayecto[0]) + "\n")

        elif numeroParadasCreadas < numeroParadas:
            texto.insert("end", "Como se necesita aumentar el número de paradas, " +
                                "se va a calcular qué tantas personas se subirían o bajarían " +
                                "en promedio para cada parada no añadida en el trayecto si " +
                                "esta fuera añadida. Luego se irán incluyendo para completar " +
                                "las paradas pedidas. Y por último se irán quitando o añadiendo " +
                                "si el conjunto de paradas añadidas aumenta más del porcentaje " +
                                "especificado.\n")
            primeraParada = trayecto[0]
            ultimaParada = trayecto[numeroParadasCreadas - 1]

            # Viendo la distancia del trayecto.
            recorridoTotal = Red.DISTANCIAS[primeraParada][ultimaParada]

            # Corrección de errores.
            if numeroParadas > len(Red.PARADAS):
                numeroParadas = len(Red.PARADAS)

            # Viendo las paradas que ya están.
            enRuta = sorted(trayecto.copy())
            noEnRuta = []
            for i in range(len(Red.PARADAS)):
                if i not in enRuta:
                    noEnRuta.append(i)

            # Viendo los flujos entrantes desde el trayecto a paradas que no están en el trayecto.
            rutaANoRuta = [0 for _ in noEnRuta]
            separacion = 0
            for i in range(len(noEnRuta)):
                separacion = Red.posicion(trayecto, noEnRuta[i])
                for j in range(len(enRuta)):
                    # Viendo si la parada en la ruta está antes o después de la parada que no está en la ruta.
                    if enRuta[j] <= separacion[0]:
                        # Si está antes, import cuántos se bajan.
                        rutaANoRuta[i] += promedios[enRuta[j]][noEnRuta[i]]
                    else:
                        # Si está despues, importa cuántos se suben.
                        rutaANoRuta[i] += promedios[noEnRuta[i]][enRuta[j]]

                # Imprimiendo los datos.
                texto.insert("end", Red.Parada(noEnRuta[i]) + " es pedido por " +
                                    str(rutaANoRuta[i]) + " personas en promedio.\n")

            # Visualizando la contribución individual de cada parada a añadir.
            contribucionIndividual = [0 for _ in range(len(noEnRuta))]
            posicion = [] # Para ver la posición que debería ocupar.
            contribucion = 0 # Distancia que contribuye.
            paradaAnterior, paradaPosterior = 0, 0 # Paradas donde se encuentra ensandwichado.
            for i in range(len(noEnRuta)):
                posicion = Red.posicion(trayecto, noEnRuta[i])

                # Separando por casos.
                if posicion[0] < 0:
                    # Se incluye la parada al inicio.
                    paradaPosterior = trayecto[posicion[1]]
                    contribucion = Red.DISTANCIAS[noEnRuta[i]][paradaPosterior]
                elif posicion[1] >= len(trayecto):
                    # Se incluye la parada al final.
                    paradaAnterior = trayecto[posicion[0]]
                    contribucion = Red.DISTANCIAS[paradaAnterior][noEnRuta[i]]
                else:
                    # Se incluye la parada en el intermedio.
                    paradaAnterior = trayecto[posicion[0]]
                    paradaPosterior = trayecto[posicion[1]]
                    contribucion = (Red.DISTANCIAS[paradaAnterior][noEnRuta[i]] +
                                    Red.DISTANCIAS[noEnRuta[i]][paradaPosterior] -
                                    Red.DISTANCIAS[paradaAnterior][paradaPosterior])

                contribucionIndividual[i] = contribucion

                texto.insert("end", "Al ubicar a " + Red.Parada(noEnRuta[i]) +
                                    " entre las ciudades " + Red.Parada(paradaAnterior) + "-" +
                                    Red.Parada(paradaPosterior) + " esta añade una distancia de " +
                                    str(contribucion) + "\n")

            # Viendo si cumple que no sobrepasa la longitud máxima deseada.
            cantidadFaltante = numeroParadas - numeroParadasCreadas
            paradasEnOrden = sorted([(i, noEnRuta[i]) for i in range(len(rutaANoRuta))],
                                    key = lambda x: x[1], reverse = True)
            paradasEnOrden = [x[0] for x in paradasEnOrden]
            nuevaParada = 0
            nuevoTrayecto = trayecto.copy()
            aporte = [0 for _ in range(cantidadFaltante)]
            for i in range(cantidadFaltante):
                nuevaParada = noEnRuta[paradasEnOrden[i]]
                nuevoTrayecto = Red.agregarParada(nuevoTrayecto, nuevaParada)
                aporte[i] = contribucionIndividual[i]
                texto.insert("end", "Añadiendo a " + Red.Parada(nuevaParada) + " con " +
                                    str(aporte[i]) + " distancia adicional.\n")

            # Viendo si cumple que no sobrepasa la longitud máxima deseada.
            nuevoRecorridoTotal = Red.longitud(nuevoTrayecto)
            ordendeAporte = []
            paradaAEliminar = 0 # Parada a eliminar en el siguiente paso.
            while (nuevoRecorridoTotal > recorridoTotal * factor) and (len(paradasEnOrden) > cantidadFaltante):
                texto.insert("end", "Como la distancia total al añadir las paradas es " +
                                    str(nuevoRecorridoTotal) + " se va a reemplazar la " +
                                    "parada que más distancia aporta.\n")

                # Eliminando la parada que más distancia individual contribuye.
                ordendeAporte = sorted([(i, aporte[i]) for i in range(len(aporte))],
                                       key = lambda x: x[1], reverse = True)
                ordendeAporte = [x[0] for x in ordendeAporte]
                paradaAEliminar = noEnRuta[paradasEnOrden[ordendeAporte[0]]]
                paradasEnOrden.pop(ordendeAporte[0])
                nuevoTrayecto = Red.eliminarParada(nuevoTrayecto, paradaAEliminar)

                # Añadiendo la siguiente parada a analizar.
                nuevaParada = noEnRuta[paradasEnOrden[cantidadFaltante - 1]]
                nuevoTrayecto = Red.agregarParada(nuevoTrayecto, nuevaParada)

                # Imprimeidno lo que pasa.
                texto.insert("end", "Cambiando " + Red.Parada(paradaAEliminar) + " por " + Red.Parada(nuevaParada) + "\n")

                # Viendo la siguiente iteración.
                aporte[ordendeAporte[0]] = contribucionIndividual[paradasEnOrden[cantidadFaltante - 1]]
                nuevoRecorridoTotal = Red.longitud(nuevoTrayecto)

            if len(paradasEnOrden) == cantidadFaltante:
                ordendeAporte.pop(0)
                cuentaRegresiva = 0
                texto.insert("end", "Como la distancia total no ha disminuido al valor " +
                                    "deseado, se van a ir eliminando paradas.\n")
                while (nuevoRecorridoTotal > recorridoTotal * factor) and cuentaRegresiva < cantidadFaltante - 1:
                    # Eliminando progresivamente las paradas.
                    paradaAEliminar = paradasEnOrden[ordendeAporte[cuentaRegresiva]]
                    nuevoTrayecto = Red.eliminarParada(nuevoTrayecto, paradaAEliminar)

                    texto.insert("end", "Eliminando " + Red.Parada(paradaAEliminar) + ".\n")

                    # Viendo la siguiente iteración.
                    nuevoRecorridoTotal = Red.longitud(nuevoTrayecto)
                    cuentaRegresiva += 1

            if numeroParadas > len(nuevoTrayecto):
                texto.insert("end", "Lo sentimos, pero el porcentaje no permitió alcanzar el número de paradas.\n")

        else:
            nuevoTrayecto = trayecto

        return nuevoTrayecto

    def creacionRuta(self):
        from Empresa import Empresa
        from Red import Red
        from Ruta import Ruta

        # Teniendo el control de la pantalla.
        frame = self.frameContenido

        # Limpiando la pantalla.
        for widget in frame.winfo_children():
            widget.destroy()

        # Implementación de la funcionalidad 4.
        # Creación del título.
        self.title("Creación de una nueva ruta.")
        fondo = tk.Frame(frame, height = 10, width = 15, bg = "lightgray", bd = 2, relief = "solid")
        fondo.pack(fill = "x", side = "top", anchor = "c", padx = 10, pady = 10)
        tk.Label(fondo, text = "Creación de una nueva ruta.", font = ("Arial", 16),
                 bg = "lightgray" ).pack(pady = 15)

        """ Idea original.
        # Creando la sección de elegir los elementos.
        frameSeleccion = tk.Frame(frame, bg = "lightgray")
        frameSeleccion.pack(side = "left", fill = "y", padx = 5, pady = 5)

        # Función para una selección dinámica.
            # Cada que se selecciona una opción en un ComboBox se cambia el texto en el Entry.
        def cambio(event, entrada: tk.Entry, combo: ttk.Combobox):
            entrada.delete(0, "end")
            entrada.insert(0, combo.get())
            # Cada que se escriba un texto en el Entry, se muestran las opciones en el ComboBox
            # que empiecen con ese texto.
        def filtro(var, index, mode, combo: ttk.Combobox,
                   opciones: list[str], string: tk.StringVar):
            texto = string.get()

            # Se muestran solo las opciones que inicien con el texto en el ComboBox.
            nuevasOpciones = []
            for opcion in opciones:
                if opcion[0 : len(texto)].lower() == texto.lower():
                    nuevasOpciones.append(opcion)
            combo['values'] = nuevasOpciones

        # Escoger una empresa.
            # Frame de esto.
        frameEmpresa = tk.Frame(frameSeleccion)
        frameEmpresa.pack(side = "top", fill = "x", padx = 5, pady = 5)

            # Título.
        tk.Label(frameEmpresa, text = "Selecciona una empresa", font = ("Arial", 8),
                 bg = "lightgray").pack(side = "top", fill = "x", pady = 5)

            # ComboBox de empresas.
        #empresas = Empresa.getEmpresas()
        empresas = ["TroleBus", "Metro", "Tren"]
        comboEmpresa = ttk.Combobox(frameEmpresa, values = empresas,
                                    textvariable = tk.StringVar(value = "Empresa"))
        #[empresa.getNombre() for empresa in empresas], textvariable = valorDefault)
        comboEmpresa.bind("<<ComboboxSelected>>", lambda x: cambio(x, entradaEmpresa, comboEmpresa))
        comboEmpresa.pack(side = "left", padx = 10, pady = 10)

            # Entry de empresas.
        stringEmpresa = tk.StringVar()
        stringEmpresa.trace_add("write", lambda var, index, mode:
                                filtro(var, index, mode, combo = comboEmpresa,
                                opciones = empresas, string = stringEmpresa))
        entradaEmpresa = tk.Entry(frameEmpresa, textvariable = stringEmpresa)
        entradaEmpresa.pack(side = "right", padx = 10, pady = 10)

        # Escoger paradas.
            # Frames.
        frameParadas       = tk.Frame(frameSeleccion)
        frameParadaSalida  = tk.Frame(frameParadas)
        frameParadaLlegada = tk.Frame(frameParadas)
        frameParadas.pack(side = "top", fill = "x", padx = 5, pady = 5)

            # Título.
        tk.Label(frameParadas, text = "Selecciona las paradas", font = ("Arial", 8),
                 bg = "lightgray" ).pack(side = "top", fill = "x", pady = 5)

            # Posicionando los frames.
        frameParadaSalida.pack(side = "top", fill = "x", padx = 5, pady = 5)
        frameParadaLlegada.pack(side = "top", fill = "x", padx = 5, pady = 5)

            # ComboBox de Paradas.
        #paradas = Red.Paradas
        paradas = ["BOGOTA", "MEDELLIN", "BARRANQUILLA", "CALI", "PEREIRA", "TUNJA"]

                # Salida
        comboParadaSalida  = ttk.Combobox(frameParadaSalida, values = paradas,
                                          textvariable = tk.StringVar(value = "Salida"))
        comboParadaSalida.bind("<<ComboboxSelected>>", lambda x: cambio(x, entradaParadaSalida, comboParadaSalida))
        comboParadaSalida.pack(side = "left", padx = 10, pady = 10)

                # Llegada
        comboParadaLlegada = ttk.Combobox(frameParadaLlegada, values = paradas,
                                          textvariable = tk.StringVar(value = "Llegada"))
        comboParadaLlegada.bind("<<ComboboxSelected>>", lambda x: cambio(x, entradaParadaLlegada, comboParadaLlegada))
        comboParadaLlegada.pack(side = "left", padx = 10, pady = 10)

            # Entry de Paradas.
                # Salida.
        stringParadaSalida = tk.StringVar()
        stringParadaSalida.trace_add("write", lambda var, index, mode:
                                     filtro(var, index, mode, combo = comboParadaSalida,
                                     opciones = paradas, string = stringParadaSalida))
        entradaParadaSalida = tk.Entry(frameParadaSalida, textvariable = stringParadaSalida)
        entradaParadaSalida.pack(side = "right", padx = 10, pady = 10)

                # Llegada.
        stringParadaLlegada = tk.StringVar()
        stringParadaLlegada.trace_add("write", lambda var, index, mode:
                                     filtro(var, index, mode, combo = comboParadaLlegada,
                                     opciones = paradas, string = stringParadaLlegada))
        entradaParadaLlegada = tk.Entry(frameParadaLlegada, textvariable = stringParadaLlegada)
        entradaParadaLlegada.pack(side = "right", padx = 10, pady = 10)

        # Mapa de Colombia.
        mapa = PhotoImage(file = "src/uiMain/Imagenes/Mapa Colombia.png", palette = 4)
        #mapa.subsample(x = 100000000, y = 100000000)
        labelMapa = tk.Label(frame, text = "Mapa", font = ("Arial", 20), fg = "black", bg = "white")
        labelMapa.config(image = mapa, compound = "bottom")
        labelMapa.pack(padx = 10, pady = 10)"""

        # Frame izquierdo
        frameResultado = tk.Frame(frame, bg = "white")
        frameResultado.pack(side = "left", fill = "y")

        # Búsqueda:
        frameBusqueda = tk.Frame(frameResultado, bg = "white")
        frameBusqueda.pack(side = "top", pady = 10, padx = 10)
            # Criterios y Frame de Búsqueda.
        criterios = ["Empresa", "Lugar origen", "Lugar destino"]
        formulario = FF.FieldFrame(frameBusqueda, "Criterio", criterios, "Valor")
        formulario.pack(side = "left", padx = 10, pady = 10)

            # Definición de los valores aceptables.
        empresas = Empresa.getEmpresas()
        paradas = Red.PARADAS.copy()

        def simplificarPalabra(palabra: str) -> str:
            # Se quitan todas las tildes y se pone en minúscula una palabra.
            palabra = palabra.lower()
            palabra = palabra.replace("á", "a")
            palabra = palabra.replace("é", "e")
            palabra = palabra.replace("í", "i")
            palabra = palabra.replace("ó", "o")
            palabra = palabra.replace("ú", "u")

            return palabra

        # Aquí tengo que arrojar el error en caso de no existir la ciudad.
            # Ingresando los datos para hacer una búsqueda.
        def datosPrincipales():
            # Borrando todas las entradas
            textoResultado.delete(1.0, "end")

            # Imprimiendo el proceso.
            textoResultado.insert(1.0, "Cargando los datos para:\n")
            inputs = [simplificarPalabra(entrada) for entrada in formulario.getEntries()]
            for i in range(len(inputs)):
                textoResultado.insert(2 * i + 2.0, formulario.criterios[i] + ": ")
                textoResultado.insert(2 * i + 3.0, inputs[i] + "\n")

            # Viendo si las opciones son correctas.
                # Lugar inicio.
            for i in range(len(paradas)):
                if simplificarPalabra(paradas[i]) == inputs[1]:
                    paradaOrigen = i
                    break
            else:
                textoResultado.insert("end", "No existe la parada " + inputs[1] + ".\n")
                textoResultado.insert("end", "Vuelva a intentar.\n")
                return None

                # Lugar destino.
            for i in range(len(paradas)):
                if simplificarPalabra(paradas[i]) == inputs[2]:
                    paradaDestino = i
                    break
            else:
                textoResultado.insert("end", "No existe la parada " + inputs[2] + ".\n")
                textoResultado.insert("end", "Vuelva a intentar.\n")
                return None

                # Empresa
            for empresa in empresas:
                if simplificarPalabra(empresa.getNombre()) == inputs[0]:
                    primerosDatos.clear()
                    # Hallando la ruta óptima.
                    trayecto = Red.algoritmoBellmanFord(paradaOrigen, paradaDestino)

                    # Mostrando la ruta óptima.
                    for ordinal in trayecto[:-1]:
                        textoResultado.insert("end", Red.Parada(ordinal) + " --> ")
                    textoResultado.insert("end", Red.Parada(trayecto[-1]) + "\n")
                    primerosDatos.append(empresa)
                    primerosDatos.append(trayecto)
                    break
            else:
                textoResultado.insert("end", "No existe la empresa " + inputs[0] + ".\n")
                textoResultado.insert("end", "Vuelva a intentar.\n")
                return None
        
        def datosAjuste():
            # Borrando todas las entradas
            textoResultado.delete(1.0, "end")

            # Imprimiendo el proceso.
            textoResultado.insert(1.0, "Cargando los datos para:\n")
            inputs = [entrada for entrada in formularioAjustes.getEntries()]
            for i in range(len(inputs)):
                textoResultado.insert(2 * i + 2.0, formularioAjustes.criterios[i] + ": ")
                textoResultado.insert(2 * i + 3.0, inputs[i] + ".\n")

            # Viendo si las opciones son correctas.
                # Número de paradas.
            try:
                inputs[0] = int(inputs[0])
            except ValueError:
                textoResultado.insert("end", "Inserte un número entero de paradas.\n")
                return None
            try:
                inputs[1] = float(inputs[1])
            except ValueError:
                textoResultado.insert("end", "Inserte un número para el factor.\n")
                return None

            # Hallando el nuevo camino.
            ruta = self.ajustarParadas(empresa = primerosDatos[0], trayecto = primerosDatos[1],
                                       numeroParadas = inputs[0], factor = inputs[1],
                                       texto = textoResultado)
            for parada in ruta:
                trayectoReal.append(parada)

        def continuarDatos():
            if len(primerosDatos) != 0:
                formulario.destroy()
                formularioAjustes.pack(side = "left", padx = 10, pady = 10)
                textoResultado.delete(1.0, "end")
                botonContinuar.config(command = continuarAjuste)
                botonInputs.config(command = datosAjuste)
            else:
                textoResultado.insert("end", "Faltan campos por rellenar.\n")

        def continuarAjuste():
            if trayectoReal is not None:
                if len(trayectoReal) != 0:
                    # Modificando la función de los botones.
                    formularioAjustes.destroy()
                    botonInputs.destroy()
                    botonBorrar.destroy()
                    botonContinuar.config(text = "Terminar", command = pasarInfo)

                    # Borrando todo el texto.
                    textoResultado.delete(1.0, "end")

                    rutaNueva = Ruta(lugarInicio = Red.Parada(trayectoReal[0]),
                                     lugarFin = Red.Parada(trayectoReal[len(trayectoReal) - 1]))
                    empresa = primerosDatos[0]
                    empresa.asignarRuta(rutaNueva)
                    textoResultado.insert("end", "Tu ruta ha sido asignada al bus:\n" +
                                          str(rutaNueva.getBusAsociado()) + "\nJunto al chofer:\n" +
                                          str(rutaNueva.getChoferAsociado()) + "\n")
                else:
                    textoResultado.insert("end", "La ruta está vacía.\n")
            else:
                textoResultado.insert("end", "No se creó su ruta correctamente.\n")

        def pasarInfo():
            for widget in frame.winfo_children():
                widget.destroy()

            # Botones.
        frameBotones = tk.Frame(frameBusqueda, bg = "black", height = 20, width = 10)
        frameBotones.pack(side = "right")
        botonInputs  = tk.Button(frameBotones, text = "Buscar", command = datosPrincipales)
        botonBorrar = tk.Button(frameBotones, text = "Borrar", command = formulario.limpiarCampos)
        botonContinuar = tk.Button(frameBotones, text = "Continuar", command = continuarDatos)
        botonInputs.pack(side = "top", padx = 10, pady = 10)
        botonContinuar.pack(side = "top", padx = 10, pady = 10)
        botonBorrar.pack(side = "bottom", padx = 10, pady = 10)

        # Resultado.
        textoResultado = tk.Text(frameResultado)
        textoResultado.pack(side = "top", fill = "x")

        # Recolectando la empresa y trayecto.
        primerosDatos = []

        # Ingresando el factor y número de paradas deseado.
        criteriosAjustes = ["Número de paradas", "Factor"]
        formularioAjustes = FF.FieldFrame(frameBusqueda, "Criterio", criteriosAjustes, "Valor")
        trayectoReal = []

        #self.title("Sistema - Ventana Principal")