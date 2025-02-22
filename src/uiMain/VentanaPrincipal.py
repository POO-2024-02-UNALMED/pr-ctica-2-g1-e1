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
            from Excepciones import InexistenciaExcepcion, CampoFaltanteEx
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
            try:
                if nombrePasajero and numeroDocumento:
                    pasajero1 = Pasajero.buscarPasajero(numeroDocumento, numeroFactura)
                    if pasajero1:
                        respuestas= pasajero1.solicitarReembolso()
                        if respuestas and len(respuestas) == 2:  # Verifica si la respuesta tiene 2 elementos
                            mensaje_reembolso = respuestas[0]
                            # Mostrar el mensaje en el frameContenido
                            tk.Label(self.frameContenido, text=mensaje_reembolso).pack(pady=10)
                    else:
                        raise InexistenciaExcepcion.InexistenciaExcepcion(valor)
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

    def ajustarParadas(self, empresa: "Empresa", trayecto: list[int], numeroParadas: int, factor: float, texto: tk.Text):
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

        # Iniciando las variables necesarias.
        promedios = empresa.flujosPromedio()
        longitud = len(trayecto)


        # Ajustando para que se tenga la cantidad de paradas deseada.
        numeroParadasCreadas = len(trayecto)
        paradasReales = [0 for _ in range(numeroParadas)]
        if numeroParadasCreadas > numeroParadas:
            texto.insert("end", "Como se necesita reducir el número de paradas, " +
                                "se va a calcular cuántas personas se bajan en la " +
                                "parada desde el origen, y se van a ir quitando en" +
                                " orden descendente de estos valores.\n")
        
            # Se buscará una ruta que maximice la cantidad de personas que usarán la ruta.
            salientes = [(0, 0) for _ in range(longitud - 2)]
            for i in range(longitud - 2):
                ordinalActual = trayecto[i + 1]
                salientes[i] = (i + 1, promedios[trayecto[0]][ordinalActual])

            # Hallando el orden de la cantidad de personas que se bajan en esa parada.
            concurrencia = sorted(salientes, key = lambda x: x[1], reverse = True)

            # Mostrando las paradas en orden de cantidad de salida.
            for i in range(len(concurrencia)):
                texto.insert("end", Red.Parada(trayecto[concurrencia[i][0]]) +
                                    " tiene " + salientes[concurrencia[i]][1] + 
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
            ultimaParada = trayecto[longitud - 1]

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
                textoResultado.insert("end", "No existe la parada " + inputs[1] + "\n")
                textoResultado.insert("end", "Vuelva a intentar")
                return None

                # Lugar destino.
            for i in range(len(paradas)):
                if simplificarPalabra(paradas[i]) == inputs[2]:
                    paradaDestino = i
                    break
            else:
                textoResultado.insert("end", "No existe la parada " + inputs[2] + "\n")
                textoResultado.insert("end", "Vuelva a intentar")
                return None

                # Empresa
            for empresa in empresas:
                if simplificarPalabra(empresa.getNombre()) == inputs[0]:
                    # Hallando la ruta óptima.
                    trayecto = Red.algoritmoBellmanFord(paradaOrigen, paradaDestino)

                    # Mostrando la ruta óptima.
                    for ordinal in trayecto[:-1]:
                        textoResultado.insert("end", Red.Parada(ordinal) + " --> ")
                    textoResultado.insert("end", Red.Parada(trayecto[-1]))
                    primerosDatos.append(empresa)
                    primerosDatos.append(trayecto)
                    break
            else:
                textoResultado.insert("end", "No existe la empresa " + inputs[0] + "\n")
                textoResultado.insert("end", "Vuelva a intentar")
                return None

        def continuarDatos():
            if len(primerosDatos) != 0:
                formulario.destroy()
                criterios = ["Número de paradas", "Factor"]
                formulario = FF.FieldFrame(frameBusqueda, "Criterio", criterios, "Valor")
                formulario.pack(side = "left", padx = 10, pady = 10)
                textoResultado.delete(1.0, "end")
                botonContinuar.config(command = continuarAjuste)

        def continuarAjuste():
            pass

            # Botones.
        frameBotones = tk.Frame(frameBusqueda, bg = "black", height = 20, width = 10)
        frameBotones.pack(side = "right")
        botonInputs  = tk.Button(frameBotones, text = "Buscar", command = datosPrincipales)
        botonContinuar = tk.Button(frameBotones, text = "Continuar", command = continuarDatos)
        botonBorrar = tk.Button(frameBotones, text = "Borrar", command = formulario.limpiarCampos)
        botonInputs.pack(side = "top", padx = 10, pady = 10)
        botonContinuar.pack(side = "top", padx = 10, pady = 10)
        botonBorrar.pack(side = "bottom", padx = 10, pady = 10)

        # Resultado.
        textoResultado = tk.Text(frameResultado)
        textoResultado.pack(side = "top", fill = "x")

        # Recolectando la empresa y trayecto.
        primerosDatos = []

        # Ingresando el factor y número de paradas deseado.
        

        #self.title("Sistema - Ventana Principal")