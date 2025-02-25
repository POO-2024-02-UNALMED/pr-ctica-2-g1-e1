from ErrorAplicacion import ErrorAplicacion
from tkinter import messagebox
class ErrorTipoDatoEx(ErrorAplicacion):
    def __init__(self, campo, tipo_esperado):
        self.campo = campo
        self.tipo_esperado = tipo_esperado
        super().__init__(f"Error en el campo '{campo}'. Se esperaba un valor de tipo {tipo_esperado}.")


    def mostrar_advertencia(self):
        messagebox.showwarning("Error de Tipo de Dato", f"Error en el campo {self.campo}. Se esperaba un valor de{self.tipo_esperado}")
        