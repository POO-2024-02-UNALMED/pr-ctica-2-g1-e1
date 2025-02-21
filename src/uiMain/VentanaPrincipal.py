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
        menuProcesos.add_command(label="Funcionalidad 1")
        menuProcesos.add_command(label="Funcionalidad 2")
        menuProcesos.add_command(label="Funcionalidad 3", command=self.mostrarReembolsos)
        menuProcesos.add_command(label = "Funcionalidad 4", command = self.creacionRuta)
        
        menuAyuda = Menu(menuBar, tearoff=0)
        menuAyuda.add_command(label="Acerca de", command=self.mostrarAutores)
        
        menuBar.add_cascade(label="Archivo", menu=menuArchivo)
        menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesos)
        menuBar.add_cascade(label="Ayuda", menu=menuAyuda)

        self.config(menu=menuBar)

    def crearWidgets(self):
        self.frameContenido = tk.Frame(self, bg="white", bd=2, relief="solid")
        self.frameContenido.pack(expand=True, fill="both", padx=10, pady=10)

    def mostrarReembolsos(self):

        for widget in self.frameContenido.winfo_children():
            widget.destroy()
        FrPrincipal= tk.Frame(self.frameContenido)
        tk.Label(FrPrincipal, text="Bienvenido al Sistema de Reembolsos de Tickets",
                 font=("Arial", 16)).pack(pady=10)

        criterios = ["Nombre en factura", "Número de documento", "Número de factura", "Número de maletas"]
        formulario = FF.FieldFrame(FrPrincipal, "Criterio", criterios, "Valor")

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
            #try:
            if nombrePasajero and numeroDocumento:
                pasajero1 = Pasajero.BuscarPasajero(numeroDocumento, numeroFactura,self.horaZero)
                if pasajero1:
                    respuestas= pasajero1.solicitarReembolso()
                    if respuestas and len(respuestas) == 2:  # Verifica si la respuesta tiene 2 elementos
                        mensaje_reembolso = respuestas[0]
                        # Mostrar el mensaje en el frameContenido
                        tk.Label(self.frameContenido, text=mensaje_reembolso).pack(pady=10)
                else:
                    print("Pasajero no encontrado.") # cambiar por exepcion que mande un warning pasajero no encontrado
            
            #except InexistenciaExcepcion as e:
            #messagebox.showerror("Error", "Pasajero no encontrado.")
            else:
                print("Error: No se encontraron el nombre o el número de documento del pasajero.")# cambiar por exepcion de CampoFaltante
            #messagebox.showerror("Error", "No se encontraron el nombre o el número de documento del pasajero.")
        def borrarCampos():
            """Limpia los campos del formulario."""
            formulario.limpiarCampos()

        def obtenerParametros():
            """Recopila los parámetros del formulario, valida los tipos y los almacena en una lista."""
            parametros = []
            for campo, entry in formulario.entries.items():
                valor = entry.get()
                #try:
                if not valor:  # Verifica si el valor está vacío
                    print(f"Error: El campo '{campo}' no puede estar vacío.") # cambiar por exepcion
                    return  # Sale de la función si un campo está vacío
                try: # este try se va
                    if campo == "Nombre en factura":
                        if not isinstance(valor, str):
                            raise ValueError("El nombre en factura debe ser una cadena de texto.")
                    elif campo == "Número de documento":
                        int(valor)  # Intenta convertir a entero, lanza ValueError si falla
                    elif campo == "Número de factura":
                        int(valor)
                    elif campo == "Número de maletas":
                        int(valor)
                    parametros.append((campo, valor))  # Agrega la tupla (campo, valor) a la lista

                #except CampoFaltanteEx:
                #especificar el campo faltante con su respectivo warning :D

                except ValueError as e: # cambiar por exepcion TipoDato
                    print(f"Error en el campo '{campo}': {e}") #Indica el error y el campo donde ocurrió 
                    return #Sale de la funcion para evitar agregar datos incorrectos.
            messagebox.showinfo("Proceso", "Su validación está en proceso.")
            analizarParametros(parametros)

        FrPrincipal.pack(pady=10, padx=10, expand=True, fill="both")
        formulario.pack(pady=10, padx=10, expand=False, fill="both")

        frame_botones = tk.Frame(FrPrincipal)
        frame_botones.pack(pady=20)  # Centra verticalmente el frame contenedor

        btnAceptar = tk.Button(frame_botones, text="Aceptar", command=obtenerParametros)
        btnAceptar.pack(side=tk.LEFT, padx=10)

        btnBorrar = tk.Button(frame_botones, text="Borrar", command=borrarCampos)
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

    def creacionRuta(self):
        from Empresa import Empresa
        from Red import Red

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
        #empresas = Empresa.getEmpresas()
        empresas = ["Rapido", "Boli", "Ali"]
        #paradas = Red.Paradas
        paradas = ["BOGOTA", "MEDELLIN", "BARRANQUILLA", "CALI", "PEREIRA", "TUNJA"]

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
        def funcionalidad4():
            # Borrando todas las entradas
            textoResultado.delete(1.0, "end")

            # Imprimiendo el proceso.
            textoResultado.insert(1.0, "Cargando los datos para:\n")
            inputs = [simplificarPalabra(entrada) for entrada in formulario.getEntries()]
            for i in range(len(inputs)):
                textoResultado.insert(2 * i + 2.0, formulario.criterios[i] + ": ")
                textoResultado.insert(2 * i + 3.0, inputs[i] + "\n")

            # Viendo si las opciones son correctas.
            error = False
                # Empresa.
            for empresa in empresas:
                if simplificarPalabra(empresa) == inputs[0]:
                    break
            else:
                error = True
                textoResultado.insert("end", "No existe la empresa " + inputs[0] + "\n")
            
                # Lugar inicio.
            for parada in paradas:
                if simplificarPalabra(parada) == inputs[1]:
                    break
            else:
                error = True
                textoResultado.insert("end", "No existe la parada " + inputs[1] + "\n")
            
                # Lugar destino.
            for parada in paradas:
                if simplificarPalabra(parada) == inputs[2]:
                    break
            else:
                error = True
                textoResultado.insert("end", "No existe la parada " + inputs[2] + "\n")

                # Impresión si surge error.
            if error:
                textoResultado.insert("end", "Vuelva a intentar")
                return None

            # Botones.
        frameBotones = tk.Frame(frameBusqueda, bg = "black", height = 20, width = 10)
        frameBotones.pack(side = "right")
        botonInputs  = tk.Button(frameBotones, text = "Buscar", command = funcionalidad4)
        bototnBorrar = tk.Button(frameBotones, text = "Borrar", command = formulario.limpiarCampos)
        botonInputs.pack(side = "top", padx = 10, pady = 10)
        bototnBorrar.pack(side = "bottom", padx = 10, pady = 10)

        # Resultado.
        textoResultado = tk.Text(frameResultado)
        textoResultado.pack(side = "top", fill = "x")

        #self.title("Sistema - Ventana Principal")