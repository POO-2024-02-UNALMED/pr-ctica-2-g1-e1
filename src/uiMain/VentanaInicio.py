from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
import VentanaPrincipal as VP


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
        botonHojaDeVida = tk.Button(p5)
        botonHojaDeVida.pack(expand=True, fill="both")
        
        tituloHojaDeVida = tk.Label(botonHojaDeVida,text="Biografia",font=("Times New Roman",50))
        tituloHojaDeVida.pack()

        
              
        nombreHojaDeVida = tk.Label(botonHojaDeVida,text="Nombre:"+" "+"Juan Camilo Moreano",font=("Times New Roman",25))
        nombreHojaDeVida.pack(side="top",pady=10)
        
        
        fechaNaHojaDeVida = tk.Label(botonHojaDeVida,text="Fecha de nacimiento:"+" "+"5 de junio de 2002",font=("Times New Roman",25))
        fechaNaHojaDeVida.pack(side="top",pady=10)
        
        
        
        descripcionHojaDeVida = tk.Label(botonHojaDeVida,text="Descripcion:"" "+"realizar descripcion",font=("Times New Roman",25))
        descripcionHojaDeVida.pack(side="top",pady=10)
        
        cambiarHojaDevida = tk.Label(botonHojaDeVida,text="Click sobre la biografia para cambiar de autor",font=("Cursiva",15),fg="blue")
        cambiarHojaDevida.pack(side="bottom",pady=10)
        

        # P6 - Fotos de desarrolladores
        # Cargar las imágenes y redimensionarlas
        def load_image(path, width, height):
            image = Image.open(path)
            image = image.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(image)

        # Tamaño deseado para las imágenes
        image_width = 150
        image_height = 150

        # Cargar las imágenes redimensionadas
        imagen1 = load_image(
            r"src\uiMain\Imagenes\foto1.png",
            image_width,
            image_height,
        )
        imagen2 = load_image(
            r"src\uiMain\Imagenes\foto2.png",
            image_width,
            image_height,
        )
        imagen3 = load_image(
            r"src\uiMain\Imagenes\foto3.png",
            image_width,
            image_height,
        )
        imagen4 = load_image(
            r"src\uiMain\Imagenes\foto4.png",
            image_width,
            image_height,
        )

        p6 = tk.Frame(p2, bg="lightblue")
        p6.pack(expand=True, fill="both", padx=5, pady=5)

        # Crear y posicionar etiquetas manualmente
        foto1 = tk.Label(p6, image=imagen1, bg="white", relief="solid")
        foto1.image = imagen1  # Evitar que se elimine la imagen
        foto1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        foto2 = tk.Label(p6, image=imagen2, bg="white", relief="solid")
        foto2.image = imagen2
        foto2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        foto3 = tk.Label(p6, image=imagen3, bg="white", relief="solid")
        foto3.image = imagen3
        foto3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        foto4 = tk.Label(p6, image=imagen4, bg="white", relief="solid")
        foto4.image = imagen4
        foto4.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        # Configurar pesos de filas y columnas para distribuir correctamente
        p6.columnconfigure(0, weight=1, uniform="group1")
        p6.columnconfigure(1, weight=1, uniform="group1")
        p6.rowconfigure(0, weight=1, uniform="group1")
        p6.rowconfigure(1, weight=1, uniform="group1")

    def cambiarImagen(self, event):
        self.imgLabel.config(text="Imagen cambiada")

    def abrirVentanaPrincipal(self):
        self.destroy()
        VP.VentanaPrincipal()