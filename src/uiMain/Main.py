import sys
import os
def importacion(direccion: str) -> None:
    sys.path.append(direccion)
    for element in os.listdir(direccion):
        if not((".git" in element) or ("__pycache__" in element)):
            if os.path.isdir(direccion + "\\" + element):
                importacion(direccion + "\\" + element)

path = os.getcwd().split("\\")
if "src" in path:
    while path[len(path) - 1] != "src":
        path.pop(len(path) - 1)
    path.pop(len(path) - 1)

path = "\\".join(path)
importacion(path)

import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Menu, messagebox, PhotoImage, ttk
from abc import ABC, abstractmethod
import pickle
import datetime

from EscritorLector import LlamarBD
import VentanaInicio as VI
from Ruta import Ruta
from Contabilidad import Contabilidad
if __name__ == "__main__":
    Pasajeros, facturas, Contabilidad ,Rutas, Buses,Choferes, empresas, asientos, maletas= LlamarBD()
    app = VI.VentanaInicio()
    app.mainloop()