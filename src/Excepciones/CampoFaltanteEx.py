from ErrorAplicacion import ErrorAplicacion
from tkinter import messagebox
class CampoFaltanteEx(Exception):
    def __init__(self, campo):
        self.campo = campo
        super().__init__(f"El campo '{campo}' falta ser llenado.")


    def mostrar_advertencia(self):
        messagebox.showwarning("Campo Faltante", f"{self.args[0]} falta ser llenado por favor ingrese un valor")  # Usa el mensaje almacenado en self.args
