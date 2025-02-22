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
from Contabilidad import Contabilidad
if __name__ == "__main__":
    Pasajeros, facturas, Contabilidad = LlamarBDPasajeros()
    Rutas,Buses,Choferes, empresas = LlamarBDRuta()
    print(Buses)

    app = VI.VentanaInicio()
    app.mainloop()