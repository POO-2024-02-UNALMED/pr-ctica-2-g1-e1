from ErrorAplicacion import ErrorAplicacion
from tkinter import messagebox
# Para el futuro.
class InexistenciaExcepcion(ErrorAplicacion):
    def __init__(self, dato):
        self.dato = dato
        if dato == "Pasajero en el sistema": # No hacer en casa XD
            super().__init__(f"No Existe el {dato} por favor ingrese nuevamente sus datos e vuelva a intentar")
        else:
            super().__init__(f"No Existe el dato llamado {dato}")


    def mostrar_advertencia(self):
        messagebox.showwarning("No existe dato", f"{self.args[0]} asegurese que sus datos este correctamente ingresados")  # Usa el mensaje almacenado en self.args
