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
        VP.VentanaPrincipal()