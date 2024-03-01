import corefiles as cf
from corefiles import Try

def AddZona(dataInventario):
    NroZona = Try('int','Ingrese el Nro de la Zona <-> ',dataInventario,'agregar')
    nombreZona = Try('str','Ingrese el Nombre de la Zona <-> ',dataInventario,'agregar')
    totalCapacidad = Try('int','Ingrese el capacidad total de la Zona <-> ',dataInventario,'agregar')
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
            opciones = '1. Nro de Zona\n2. Nombre de la Zona\n3. Capacidad Total\n4. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personal'][codCampus]
            if (op=='1'):
                nuevoValor= Try('int','Ingrese el nuevo valor para el Nro de la zona <-> ',dataInventario,'')
                editar['NroZona'] = nuevoValor
            elif (op=='2'):
                nuevoValor= Try('str','Ingrese el nuevo valor para el nombre de la zona <-> ',dataInventario,'')
                editar['nombreZona'] = nuevoValor
            elif (op=='3'):
                nuevoValor= Try('str','Ingrese el nuevo valor para la capacidad total <-> ',dataInventario,'')
                editar['totalCapacidadd'] = nuevoValor
            elif (op=='4'):
                break
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()
