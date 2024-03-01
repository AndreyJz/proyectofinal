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

def Try(type, msg, inventario):
    while True:
        try:
            Msg = input(msg)
            if(type == 'int'):
                Msg = int(Msg)
            if(type == 'float'):
                Msg = float(Msg)
            if(type == 'str'):
                Msg = str(Msg)
        except ValueError:
            print('El dato ingresado no esta permitido')
        else:
            if(type == 'str')and(len(Msg)<0):
                print('Debes ingresar un valor...')
            else:
                return Msg
                False

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

def delOp(dataInventario,opcion):
    borrar_pantalla()
    if opcion == 'activo':
        delVal = Try('str', "Ingrese el Codigo de campus del Activo que quiere borrar <-> ", dataInventario[opcion])
    elif opcion == 'personas':
        delVal = Try('int', "Ingrese el Nro de Identificacion de la Persona que quiere borrar <-> ", dataInventario[opcion])
    elif opcion == 'zonas':
        delVal = Try('str', "Ingrese el Nro de Identificacion de la Zona que quiere borrar <-> ", dataInventario[opcion])

    dataInventario[opcion].pop(delVal)
    updateData('data.json',dataInventario)
    print('Ha sido eliminado correctamente')
    pausar_pantalla()


def Search(inventario: dict, opcion: str): 
    isValueTrue = True
    while isValueTrue:
        codCampus = Try('str', ')_', inventario)
        for idx, (key, value) in enumerate(inventario[opcion].items()): #Itera sobre el diccionario seleccionado y idx imprime un mensaje de error
            if opcion == 'activos':
                if value['codCampus'] == codCampus:
                    return key
                elif len(inventario[opcion])-1 == idx:
                    print('nombre no encontrado, ingreselo de nuevo')
                    pausar_pantalla()
            elif opcion == 'personas':
                if value['id'] == codCampus:
                    return key
                elif len(inventario[opcion])-1 == idx:
                    print('Id no encontrado, ingreselo de nuevo')
                    pausar_pantalla()
            elif opcion == 'zonas':
                if value['NroZona'] == codCampus:
                    return key
                elif len(inventario[opcion])-1 == idx:
                    print('Nro de Zona no encontrado, ingreselo de nuevo')
                    pausar_pantalla()
            elif opcion == 'asignacion':
                if value['NroAsig'] == codCampus:
                    return key
                elif len(inventario[opcion])-1 == idx:
                    print('Nro de Asignacion no encontrado, ingreselo de nuevo')
                    pausar_pantalla()