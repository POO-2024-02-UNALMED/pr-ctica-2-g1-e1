import sys
import os
def recursion(direccion: str) -> None:
    sys.path.append(direccion)
    for element in os.listdir(direccion):
        if not((".git" in element) or ("__pycache__" in element)):
            if os.path.isdir(direccion + "\\" + element):
                recursion(direccion + "\\" + element)

recursion(os.getcwd())

import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk

import VentanaInicio as VI
from Contabilidad import Contabilidad
from Empresa import Empresa
from Red import Red

if __name__ == "__main__":
    #app = VI.VentanaInicio()
    #app.mainloop()
    a = 0