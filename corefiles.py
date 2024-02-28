from tabulate import tabulate
import sys
import os
import json
BASE="data/"

def borrar_pantalla(): #funcion borrar pantalla (cualquier plataforma)
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla(): #funcion pausar pantalla (cualquier plataforma)
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

def checkFile(archivo:str, data): #comprueba si el archivo existe
    if(os.path.isfile(BASE+ archivo)): 
        with open(BASE + archivo, 'r') as br: #si existe lo carga
            data = json.load(br)
            return data
    else: 
        with open(BASE + archivo ,"w") as bw: #si no existe lo crea
            json.dump(data,bw,indent=4)
            return data

def updateData(archivo:str,data): #actualiza el diccionario
    with open(BASE+archivo,"r+") as rwf:
        json.dump(data,rwf,indent=4)
        rwf.truncate() #se asegura de que no queden archivos antiguos
        
