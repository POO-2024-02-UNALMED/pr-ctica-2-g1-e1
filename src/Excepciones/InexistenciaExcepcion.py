from ErrorAplicacion import ErrorAplicacion
from tkinter import messagebox
# Para el futuro.
class InexistenciaExcepcion(Exception):
    def __init__(self, dato):
        self.dato = dato
        super().__init__(f"No Existe el dato llamado {dato}")


    def mostrar_advertencia(self):
        messagebox.showwarning("No existe dato", f"{self.args[0]} asegurese que sus datos este correctamente ingresados")  # Usa el mensaje almacenado en self.args
