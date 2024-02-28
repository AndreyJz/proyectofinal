import corefiles as cf


def AddZona(dataInventario):
    NroZona = input('Ingrese el Nro de la Zona <-> ')
    nombreZona = input('Ingrese el Nombre de la Zona <-> ')
    totalCapacidad = input('Ingrese el capacidad total de la Zona <-> ')
    Zone = {
        'NroZona':NroZona,
        'nombreZona':nombreZona,
        'totalCapacidad':totalCapacidad,
    }
    dataInventario.get('zonas').update({NroZona:Zone})


def EditZona(dataInventario):
    if dataInventario['zonas']:
        print('ingresa el Nro de Zona que desees editar :')
        codCampus= cf.Search(dataInventario, 'zonas')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. Nro de Zona\n2. Nombre de la Zona\n3. Capacidad Total\n4. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personal'][codCampus]
            if (op=='1'):
                nuevoValor= int(input('Ingrese el nuevo valor para el Id <-> '))
                editar['NroZona'] = nuevoValor
            elif (op=='2'):
                nuevoValor= str(input('Ingrese el nuevo valor para el Id <-> '))
                editar['nombreZona'] = nuevoValor
            elif (op=='3'):
                nuevoValor= str(input('Ingrese el nuevo valor para el Id <-> '))
                editar['totalCapacidadd'] = nuevoValor
            elif (op=='4'):
                break
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()
