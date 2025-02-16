import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
#from ..gestorAplicacion.administracion.Contabilidad import Contabilidad
#from ..gestorAplicacion.administracion.Empresa import Empresa
#from ..gestorAplicacion.administracion.Red import Red

class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.title("Sistema - Ventana de Inicio")
        self.geometry(f"{screenWidth}x{screenHeight}")
        self.configure(padx=5, pady=5)
        self.configurarMenu()
        self.crearEstructura()

    def configurarMenu(self):
        menuBar = Menu(self)

        menuInicio = Menu(menuBar, tearoff=0 )
        menuInicio.add_command(
            label="Descripción del sistema", command=self.mostrarDescripcion,background=""
        )
        menuInicio.add_separator()
        menuInicio.add_command(label="Salir", command=self.quit)

        menuBar.add_cascade(label="Inicio", menu=menuInicio)
        self.config(menu=menuBar)

    def mostrarDescripcion(self):
        messagebox.showinfo(
            "Descripción",
            "Esta es una aplicación para gestionar el sistema basado en la práctica 1.",
        )

    def crearEstructura(self):
        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)
        self.rowconfigure(0, weight=1)  # Adjusted to fill available space
        self.rowconfigure(1, weight=0)  # Set to 0 to avoid extra space

        # P1 - Contiene P3 y P4
        p1 = tk.Frame(self, bg="lightgray", bd=2, relief="solid")
        p1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # P3 - Saludo del sistema
        p3 = tk.Frame(p1, bg="lightgray")
        p3.pack(expand=True, fill="both", padx=5, pady=5)
        tk.Label(p3, text="Bienvenido al sistema", font=("Arial", 16)).pack(pady=10)

        # P4 - Imágenes asociadas y botón de ingreso
        p4 = tk.Frame(p1, bg="gray")
        p4.pack(expand=True, fill="both", padx=5, pady=5)
        self.imgLabel = tk.Label(p4, text="Imagen aquí", bg="white", relief="solid")
        self.imgLabel.pack(pady=10)
        self.imgLabel.bind("<Enter>", self.cambiarImagen)

        btnIngresar = tk.Button(
            p4, text="Ingresar", command=self.abrirVentanaPrincipal
        )
        btnIngresar.pack(pady=20)

        # P2 - Contiene P5 y P6
        p2 = tk.Frame(self, bg="white", bd=2, relief="solid")
        p2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # P5 - Hoja de vida de desarrolladores (solo lectura)
        p5 = tk.Frame(p2, bg="white")
        p5.pack(expand=True, fill="both", padx=5, pady=5)
        hojaDeVida = tk.Label(
            p5,
            text="Aquí se mostrará la hoja de vida de los desarrolladores",
            wraplength=300,
            justify="left",
        )
        hojaDeVida.pack(expand=True, fill="both")

        # P6 - Fotos de desarrolladores
        p6 = tk.Frame(p2, bg="lightblue")
        p6.pack(expand=True, fill="both", padx=5, pady=5)
        for i in range(2):
            for j in range(2):
                tk.Label(p6, text=f"Foto {i*2+j+1}", bg="white", relief="solid").grid(
                    row=i, column=j, padx=5, pady=5, sticky="nsew")
                p6.columnconfigure(j, weight=1)
            p6.rowconfigure(i, weight=1)

    def cambiarImagen(self, event):
        self.imgLabel.config(text="Imagen cambiada")

    def abrirVentanaPrincipal(self):
        self.destroy()
        VentanaPrincipal()

class FieldFrame(tk.Frame):
    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(parent, bd=2, relief="solid")
        self.criterios = criterios
        self.valores = valores if valores else ["" for _ in criterios]
        self.habilitado = habilitado if habilitado else [True for _ in criterios]
        
        tk.Label(self, text=tituloCriterios, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text=tituloValores, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)
        
        self.entries = {}
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(self)
            entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
            entry.insert(0, self.valores[i])
            if not self.habilitado[i]:
                entry.config(state="disabled")
            self.entries[criterio] = entry
        
        self.columnconfigure(1, weight=1)
    
    def getValue(self, criterio):
        return self.entries[criterio].get() if criterio in self.entries else None

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
        formulario = FieldFrame(self.frameContenido, "Criterio", criterios, "Valor")
        formulario.pack(pady=10, padx=10, expand=True, fill="both")

    def mostrarInfo(self):
        messagebox.showinfo("Información", "El proyecto se centra en crear una herramienta con la cual se establezca una comunicación entre los usuarios de una terminal de buses y las empresas de dicha terminal de manera que se sistematice los procesos más comunes que involucran a ambos.")
    
    def mostrarAutores(self):
        messagebox.showinfo("Autores", "Desarrollado por un equipo de desarrolladores integrado por. Salcedo Rodriguez Santiago Abelardo  , Cardona Ramirez Luis Mario, Rincon Stiven Brandon, Ceron Quintero David Fernando, Moreano Urresty Juan Camilo.")
    
    def cerrarSesion(self):
        self.destroy()
        VentanaInicio()

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
                if opcion[0 : len(texto)] == texto:
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
        string = tk.StringVar()
        string.trace_add("write", lambda var, index, mode: filtro(var, index, mode, combo = comboEmpresa,
                                                                  opciones = empresas, string = string))
        entradaEmpresa = tk.Entry(frameEmpresa, textvariable = string)
        entradaEmpresa.pack(side = "right", padx = 10, pady = 10)

        # Escoger paradas.
            # Frame.
        frameParadas = tk.Frame(frameSeleccion)
        frameParadas.pack(side = "top", fill = "x", padx = 5, pady = 5)

            # Título.
        tk.Label(frameParadas, text = "Selecciona las paradas", font = ("Arial", 8),
                 bg = "lightgray" ).pack(side = "top", fill = "x", pady = 5)

            # 
        #paradas = Red.Paradas
        paradas = ["BOGOTA", "MEDELLIN", "BARRANQUILLA", "CALI", "PEREIRA", "TUNJA"]
        comboParadaSalida  = ttk.Combobox(frameParadas, values = paradas,
                                          textvariable = tk.StringVar(value = "Salida"))
        comboParadaLlegada = ttk.Combobox(frameParadas, values = paradas,
                                          textvariable = tk.StringVar(value = "Llegada"))

        self.title("Sistema - Ventana Principal")

if __name__ == "__main__":
    app = VentanaInicio()
    app.mainloop()