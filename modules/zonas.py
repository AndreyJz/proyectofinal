import corefiles as cf
from corefiles import Try

def AddZona(dataInventario):
    NroZona = str(len(dataInventario['zonas'])+1).zfill(2)
    newNroZona = 0
    for keys in dataInventario['zonas'].keys():
        if NroZona == keys:
            NroZona = str(newNroZona + 1).zfill(2)
    nombreZona = Try('str','Ingrese el Nombre de la Zona <-> ',dataInventario)
    totalCapacidad = Try('int','Ingrese el capacidad total de la Zona <-> ',dataInventario)
    Zone = {
        'NroZona':NroZona,
        'nombreZona':nombreZona,
        'totalCapacidad':totalCapacidad,
    }
    dataInventario.get('zonas').update({NroZona:Zone})


def EditZona(dataInventario):
    if dataInventario['zonas']:
        print('Ingresa el Nro de Zona que desees editar <-> ')
        codCampus= cf.Search(dataInventario, 'zonas')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. Nombre de la Zona\n2. Capacidad Total\n3. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personal'][codCampus]
            if (op=='1'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el nombre de la zona <-> ',dataInventario,)
                editar['nombreZona'] = nuevoValor
            elif (op=='2'):
                nuevoValor= Try('str','Ingrese el nuevo valor para la capacidad total <-> ',dataInventario,)
                editar['totalCapacidadd'] = nuevoValor
            elif (op=='3'):
                break
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()
