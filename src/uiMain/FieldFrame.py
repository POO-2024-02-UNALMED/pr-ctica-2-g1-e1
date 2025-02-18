import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk



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
    
    def getValue(self, criterio: str):
        return self.entries[criterio].get() if criterio in self.entries else None

    def getEntries(self):
        """
        Devuelve todas los inputs puestos.
        """

        return [self.getValue(criterio) for criterio in self.criterios]

    def limpiarCampos(self):
        """Limpia el contenido de todos los campos de entrada."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)  # Borra el contenido del Entry
