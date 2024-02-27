from tabulate import tabulate
import sys
import os
import json
BASE="data/"

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

def checkFile(archivo:str, data):
    if(os.path.isfile(BASE+ archivo)):
        with open(BASE + archivo, 'r') as br:
            data = json.load(br)
            return data
    else: 
        with open(BASE + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)
            return data

def updateData(archivo:str,data):
    with open(BASE+archivo,"r+") as rwf:
        rwf.seek(0)
        json.dump(data,rwf,indent=4)
        rwf.truncate()
        
def Search(inventario = dict):
    tabla = []
    for values in inventario.values():
        tabla.append([values['nit'], values['nombrePro']])
        borrar_pantalla()
        print(tabulate(tabla, tablefmt='grid'))
    nit = str(input(')_'))
    for idx, (key, value) in enumerate(inventario.items()):
        if value['nit'] == nit:
            return key
        elif idx == len(inventario)-1:
            print('nombre no encontrado')
            pausar_pantalla()