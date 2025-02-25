
import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
import VentanaPrincipal as VP
import Datos_biografias
from PIL import Image, ImageTk
class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.biografias = Datos_biografias.biografias
        self.index = 0  # Índice para recorrer biografías
        
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
        
        p5 = tk.Frame(p2, bg="white")
        p5.pack(expand=True, fill="both", padx=5, pady=5)

        self.botonHojaDeVida = tk.Frame(p5)
        self.botonHojaDeVida.pack(expand=True, fill="both")

        # Texto "Biografía" clickeable
        tituloHojaDeVida = tk.Label(
            self.botonHojaDeVida,
            text="Biografía",
            font=("Times New Roman", 50),
            fg="blue",
            cursor="hand2",
        )
        tituloHojaDeVida.pack()
        tituloHojaDeVida.bind("<Button-1>", lambda event: self.recorrerBiografias())

        self.p6 = tk.Frame(
            p2, bg="lightblue", width=600, height=300
        )  # Se establece un tamaño fijo
        self.p6.pack_propagate(False)  # Evita que el tamaño cambie automáticamente
        self.p6.pack(expand=False, fill="both", padx=5, pady=5)

        self.cargarBiografia()


        self.cargarImagenes()

    def recorrerBiografias(self):
        """Actualiza la información de la biografía."""
        self.index = (self.index + 1) % len(self.biografias)
        self.cargarBiografia()

    def cargarBiografia(self):
        """Carga la información de la biografía actual sin modificar el Frame padre."""
        for widget in self.botonHojaDeVida.winfo_children():
            widget.destroy()

        # Mantén el título fijo
        tituloHojaDeVida = tk.Label(
            self.botonHojaDeVida,
            text="Biografía",
            font=("Times New Roman", 50),
            fg="blue",
            cursor="hand2",
        wraplength=500)
        tituloHojaDeVida.pack()
        tituloHojaDeVida.bind("<Button-1>", lambda event: self.recorrerBiografias())

        # Obtener la biografía actual
        biografia = self.biografias[self.index]

        # Crear los nuevos labels pero sin modificar el tamaño del Frame padre
        tk.Label(
            self.botonHojaDeVida,
            text=f"Nombre: {biografia['nombre']}",
            font=("Times New Roman", 20),
        wraplength=500).pack(fill="none", expand=False, anchor="center", padx=5, pady=5)
        
        tk.Label(
            self.botonHojaDeVida,
            text=f"Fecha de nacimiento: {biografia['fechaNacimiento']}",
            font=("Times New Roman", 20),
        wraplength=500).pack(fill="none", expand=False, anchor="center", padx=5, pady=5)
        tk.Label(
            self.botonHojaDeVida,
            text=f"Descripción:\n{biografia['descripcion']}",
            font=("Times New Roman", 20),
        wraplength=500).pack(fill="none", expand=False, anchor="center", padx=5, pady=5)
        
        tk.Label(
            self.botonHojaDeVida,
            text=f"Presionar sobre BIOGRAFIA para cambiar",
            font=("cursiva", 15),
            fg="red",
        wraplength=500).pack(side="bottom", fill="none", expand=False, anchor="center", padx=5, pady=5)

        self.cargarImagenes()
        
        
#########
    def load_image(self, path, width, height):
        """Carga y redimensiona imágenes."""
        try:
            image = Image.open(path)
            image = image.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error al cargar la imagen {path}: {e}")
            return None
########


    def cargarImagenes(self):
        """Carga las imágenes de la biografía actual y las distribuye de manera uniforme."""
        for widget in self.p6.winfo_children():
            widget.destroy()

        biografia = self.biografias[self.index]

        columnas = 2
        filas = 2
        width = self.p6.winfo_width() // columnas
        height = self.p6.winfo_height() // filas

        if width == 0 or height == 0:
            width = 250
            height = 250
            
        else:
            width = 250
            height = 250
            
        if not hasattr(self, "imagenes"):
            self.imagenes = {}

        for i in range(1, 5):
            img_path = biografia[f"imagen{i}"]
            if img_path not in self.imagenes:
                self.imagenes[img_path] = self.load_image(img_path, width, height)

            imagen_label = tk.Label(self.p6, image=self.imagenes[img_path], bg="white")
            imagen_label.image = self.imagenes[img_path]
            imagen_label.grid(
                row=(i - 1) // columnas,
                column=(i - 1) % columnas,
                padx=5,
                pady=5,
                sticky="nsew",
            )

        for col in range(columnas):
            self.p6.columnconfigure(col, weight=1)
        for row in range(filas):
            self.p6.rowconfigure(row, weight=1)

    def cambiarImagen(self, event):
        """Cambia el texto de la imagen en `p4`."""
        self.imgLabel.config(text="Imagen cambiada")

    def abrirVentanaPrincipal(self):
        """Abre la ventana principal."""
        self.destroy()
        VP.VentanaPrincipal()