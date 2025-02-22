import sys
import os
def importacion(direccion: str) -> None:
    sys.path.append(direccion)
    for element in os.listdir(direccion):
        if not((".git" in element) or ("__pycache__" in element)):
            if os.path.isdir(direccion + "\\" + element):
                importacion(direccion + "\\" + element)

importacion(os.getcwd())

import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
from EscritorLector import LlamarBDPasajeros, LlamarBDRuta
import VentanaInicio as VI
from Ruta import Ruta
if __name__ == "__main__":
    Pasajeros = LlamarBDPasajeros()
    Rutas = LlamarBDRuta()
    #print(Ruta._rutas)

    app = VI.VentanaInicio()
    app.mainloop()