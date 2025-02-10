import tkinter as tk
from tkinter import Menu, messagebox
from tkinter import PhotoImage


class VentanaInicio(tk.Tk):

    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("Sistema - Ventana de Inicio")
        self.geometry(f"{screen_width}x{screen_height}")
        self.configure(padx=5, pady=5)
        self.configurar_menu()
        self.crear_estructura()

    def configurar_menu(self):
        menu_bar = Menu(self)

        menu_inicio = Menu(menu_bar, tearoff=0)
        menu_inicio.add_command(
            label="Descripción del sistema", command=self.mostrar_descripcion,background=""
        )
        menu_inicio.add_separator()
        menu_inicio.add_command(label="Salir", command=self.quit)

        menu_bar.add_cascade(label="Inicio", menu=menu_inicio)
        self.config(menu=menu_bar)

    def mostrar_descripcion(self):
        messagebox.showinfo(
            "Descripción",
            "Esta es una aplicación para gestionar el sistema basado en la práctica 1.",
        )

    def crear_estructura(self):
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
        self.img_label = tk.Label(p4, text="Imagen aquí", bg="white", relief="solid")
        self.img_label.pack(pady=10)
        self.img_label.bind("<Enter>", self.cambiar_imagen)

        btn_ingresar = tk.Button(
            p4, text="Ingresar", command=self.abrir_ventana_principal
        )
        btn_ingresar.pack(pady=20)

        # P2 - Contiene P5 y P6
        p2 = tk.Frame(self, bg="white", bd=2, relief="solid")
        p2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # P5 - Hoja de vida de desarrolladores (solo lectura)
        p5 = tk.Frame(p2, bg="white")
        p5.pack(expand=True, fill="both", padx=5, pady=5)
        hoja_vida = tk.Label(
            p5,
            text="Aquí se mostrará la hoja de vida de los desarrolladores",
            wraplength=300,
            justify="left",
        )
        hoja_vida.pack(expand=True, fill="both")

        # P6 - Fotos de desarrolladores
        p6 = tk.Frame(p2, bg="lightblue")
        p6.pack(expand=True, fill="both", padx=5, pady=5)
        for i in range(2):
            for j in range(2):
                tk.Label(p6, text=f"Foto {i*2+j+1}", bg="white", relief="solid").grid(
                    row=i, column=j, padx=5, pady=5, sticky="nsew"
                )
                p6.columnconfigure(j, weight=1)
            p6.rowconfigure(i, weight=1)

    def cambiar_imagen(self, event):
        self.img_label.config(text="Imagen cambiada")

    def abrir_ventana_principal(self):
        self.destroy()
        VentanaPrincipal()


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("Sistema - Ventana Principal")
        self.geometry(f"{screen_width}x{screen_height}")
        self.configurar_menu()
        self.crear_widgets()

    def configurar_menu(self):
        menu_bar = Menu(self, font="Arial")

        menu_archivo = Menu(menu_bar, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.cerrar_sesion)

        menu_procesos = Menu(menu_bar, tearoff=0)
        menu_procesos.add_command(label="Funcionalidad 1")
        menu_procesos.add_command(label="Funcionalidad 2")

        menu_ayuda = Menu(menu_bar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)

        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_bar.add_cascade(label="Procesos y Consultas", menu=menu_procesos)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.config(menu=menu_bar)

    def crear_widgets(self):
        tk.Label(self, text="Ventana Principal", font=("Arial", 18)).pack(pady=20)

    def mostrar_info(self):
        messagebox.showinfo("Información", "Esta es la ventana principal del sistema.")

    def mostrar_autores(self):
        messagebox.showinfo("Autores", "Desarrollado por el equipo de la práctica 2.")

    def cerrar_sesion(self):
        self.destroy()
        VentanaInicio()


if __name__ == "__main__":
    app = VentanaInicio()
    app.mainloop()
