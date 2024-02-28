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

def delOp(dataInventario,opcion):
    if dataInventario[opcion]:
        borrar_pantalla()
        if opcion == 'activo':
            delVal = input("Ingrese el Codigo de campus del Activo que quiere borrar <-> ")
        elif opcion == 'personal':
            delVal = input("Ingrese el Nro de Identificacion de la Persona que quiere borrar <-> ")
        elif opcion == 'zonas':
            delVal = input("Ingrese el Nro de Identificacion de la Zona que quiere borrar <-> ")

        if delVal not in dataInventario[opcion].items():
            print('El codigo ingresado no esta registrado...')
            os.system('pause')
            delOp()
        dataInventario[opcion].pop(delVal)
        updateData('inventario.json',dataInventario)
        print('Ha sido eliminado correctamente')
        pausar_pantalla()
    else:
        print(f'No has ingresado algun {opcion}...')
        os.system('pause')


def Search(inventario: dict, opcion: str): 
    if inventario[opcion]:
        isValueTrue = True
        while isValueTrue:
            codCampus = str(input(')_'))
            for idx, (key, value) in enumerate(inventario[opcion].items()): #Itera sobre el diccionario seleccionado y idx imprime un mensaje de error
                if opcion == 'activos':
                    if value['codCampus'] == codCampus:
                        return key
                    elif len(inventario[opcion])-1 == idx:
                        print('nombre no encontrado, ingreselo de nuevo')
                        pausar_pantalla()
                elif opcion == 'personal':
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
    else:
        print('no has ingresado ningun activo')
        pausar_pantalla()
        return
            
