import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
import FieldFrame as FF
import VentanaInicio as VI



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.title("Sistema - Ventana Principal")
        self.geometry(f"{screenWidth}x{screenHeight}")
        self.configurarMenu()
        self.crearWidgets()
    
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

        tk.Label(self.frameContenido, text="Bienvenido al Sistema de Reembolsos de Tickets",
                 font=("Arial", 16)).pack(pady=10)

        criterios = ["Nombre en factura", "Número de documento", "Número de factura", "Número de maletas"]
        formulario = FF.FieldFrame(self.frameContenido, "Criterio", criterios, "Valor")
        formulario.pack(pady=10, padx=10, expand=True, fill="both")

    def mostrarInfo(self):
        messagebox.showinfo("Información", "El proyecto se centra en crear una herramienta con la cual se establezca una comunicación entre los usuarios de una terminal de buses y las empresas de dicha terminal de manera que se sistematice los procesos más comunes que involucran a ambos.")
    
    def mostrarAutores(self):
        messagebox.showinfo("Autores", "Desarrollado por un equipo de desarrolladores integrado por. Salcedo Rodriguez Santiago Abelardo  , Cardona Ramirez Luis Mario, Rincon Stiven Brandon, Ceron Quintero David Fernando, Moreano Urresty Juan Camilo.")
    
    def cerrarSesion(self):
        self.destroy()
        VI.VentanaInicio()

    def creacionRuta(self):
        # Teniendo el control de la pantalla.
        frame = self.frameContenido

        # Limpiando la pantalla.
        for widget in frame.winfo_children():
            widget.destroy()

        # Implementación de la funcionalidad 4.
        # Creación del título.
        self.title("Creación de una nueva ruta.")
        fondo = tk.Frame(frame, height = 10, width = 15, bg = "lightgray", bd = 2, relief = "solid")
        fondo.pack(side = "top", anchor = "c", padx = 10, pady = 10)
        tk.Label(fondo, text = "Creación de una nueva ruta.", font = ("Arial", 16),
                 bg = "lightgray" ).pack(pady = 15)

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
        labelMapa.pack(padx = 10, pady = 10)

        #self.title("Sistema - Ventana Principal")