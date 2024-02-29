import corefiles as cf
from datetime import datetime

datenow = str(datetime.now())

def AddPersona(dataInventario):
    id = input('Ingrese el Nro de Id <-> ')
    nombre = input('Ingrese el Nombre <-> ')
    email = input('Ingrese el email <-> ')
    movil = input('Ingrese el Nro del movil <-> ')
    casa = input('Ingrese el Nro de telefono de su casa <-> ')
    personal = input('Ingrese el Nro de telefono personal <-> ')
    oficina = input('Ingrese el Nro de telefono de la oficina <-> ')
    Person = {
        'id':id,
        'nombre':nombre,
        'email':email,
        'telefono':{
            'movil':movil,
            'casa':casa,
            'personal':personal,
            'oficina':oficina
        }
    }
    dataInventario.get('personas').update({id:Person})


def EditPersona(dataInventario):
    if dataInventario['personas']:
        print('ingresa el Id de la persona que desees editar :')
        codCampus= cf.Search(dataInventario, 'personas')
        isValueTrue = True
        while isValueTrue:
            cf.borrar_pantalla()
            opciones = '1. ID\n2. Nombre\n3. Email\n4. telefono\n5. Salir'
            print(opciones)
            op = input('Ingrese el numero de la seccion que quiere editar <-> ')
            editar = dataInventario['personas'][codCampus]
            if (op=='1'):
                nuevoValor= int(input('Ingrese el nuevo valor para el Id <-> '))
                editar['id'] = nuevoValor
            elif (op=='2'):
                nuevoValor= str(input('Ingrese el nuevo valor para el nombre <-> '))
                editar['nombre'] = nuevoValor
            elif (op=='3'):
                nuevoValor= str(input('Ingrese el nuevo valor para el email <-> '))
                editar['email'] = nuevoValor
            elif (op=='4'):
                opciones = '1. Movil\n2. Casa\n3. Personal\n4. Oficina\n5. Salir'
                print(opciones)
                op = input('Ingrese el numero de la seccion que quiere editar <-> ')
                editar = dataInventario['personas'][codCampus]['telefono']
                if (op == '1'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el movil <-> '))
                    editar['movil'] = nuevoValor
                elif (op == '2'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro de Casa <-> '))
                    editar['casa'] = nuevoValor
                elif (op == '3'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro personal <-> '))
                    editar['personal'] = nuevoValor
                elif (op == '4'):
                    nuevoValor= str(input('Ingrese el nuevo valor para el Nro de Oficina <-> '))
                    editar['oficina'] = nuevoValor
            elif (op=='5'):
                break
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()


countAsig=0

def AddAsig(dataInventario):
    countAsig +=1
    NroAsig = str(countAsig).zfill(3) 
    fechaAsig = input('Ingrese la fecha de la Asignacion <-> ')
    opciones = '1. Persona\n2. Zona'
    print(opciones)
    tipoAsig = input('Ingrese el tipo de la asignacion <-> ')
    if tipoAsig == 'personas':
        for key,value in dataInventario['personas'].items():
            print(f'{key} -- {value["nombre"]}')
        AsignadoA = input('Ingrese el id de la persona que le asignara <-> ')
    elif tipoAsig == 'zonas':
        for key,value in dataInventario['zonas'].items():
            print(f'{key} -- {value["nombreZona"]}')
        AsignadoA = input('Ingrese el Nro de la zona que le asignara <-> ')
    Activos = []
    lstNotAsig=[]
    while True: #Ciclo para listar los Activos que no se encuentran asignados
        for key,value in dataInventario['activos'].items():
            if dataInventario['activos'][key]['Estado'] == 'no asignado':
                print(f'{key} -- {value["nombre"]}')
                lstNotAsig.append(key)
        Activo = input('Estos son los Activos que no se encuentran asigados seleccione uno ingresando el id <-> ')
        if Activo not in lstNotAsig: 
            print('El valor ingresado no esta en la lista mostrada...')
            cf.pausarpantalla()
        else:
            Activos.append(Activo)
            dataInventario['activos'][Activo]['Estado'] = 'asignado'
        if not bool(input('Desea seguir asignando Activos? S(si) o Enter(no) -> ')):
            if len(Activos) == 0:
                print('Debe asignar al menos un activo...')
                cf.pausarpantalla()
            else:
                break
    Asig={
        'NroAsig':NroAsig,
        'fechaAsig':fechaAsig,
        'tipoAsig':tipoAsig,
        'asignadoA':AsignadoA,
        'activos':Activos
    }
    dataInventario.get('asignacion').update({NroAsig:Asig})
    countAsig = len(dataInventario['activos']['historialActivo'])+1
    NroAsig = str(countAsig).zfill(3) 
    History={
        'NroId':NroAsig,
        'fecha':fechaAsig,
        'tipoMov':'asignacion',
        'idRespMov':input('Ingrese el id de la persona que realizo el movimiento <-> ')
    }
    dataInventario['activos'][Activo]['historialActivo'].update({NroAsig:History})
    
def DardeBaja(inventario):
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Dado de baja')

def GarantiaAct(inventario):
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Reparacion/Garantia')

def ReAsig(inventario,codCampus):
    Historial(inventario, codCampus, 'ReAsignado')

def ChangeAsig(inventario):
    if inventario['personas']:
        print('ingresa el Codigo del activo que desees editar :')
        codCampus = cf.Search(inventario, 'activos')
        for key,value in inventario['asignacion'].items():
            if codCampus == value['asignadoA']:
                isValueTrue = True
                while isValueTrue:
                    cf.borrar_pantalla()
                    opciones = '1. Tipo de Modificacion\n2. Id del Responsable del Mov\n3. Salir'
                    print(opciones)
                    op = input('Ingrese el numero de la seccion que quiere editar <-> ')
                    editar = inventario['asignacion'][key]
                    if (op=='1'):
                        print('Ingrese el nuevo valor para el tipo de modificacion <-> ')
                        opciones = '1. Persona\n2. Zona'
                        print(opciones)
                        tipoAsig = input('Ingrese el tipo de la asignacion <-> ')
                        if tipoAsig == 'personas':
                            for key,value in inventario['personas'].items():
                                print(f'{key} -- {value["nombre"]}')
                            nuevoValor = input('Ingrese el id de la persona que le asignara <-> ')
                        elif tipoAsig == 'zonas':
                            for key,value in inventario['zonas'].items():
                                print(f'{key} -- {value["nombreZona"]}')
                            nuevoValor = input('Ingrese el Nro de la zona que le asignara <-> ')
#editado el tipo
                        editar['tipoMov'] = nuevoValor

                    elif (op=='2'):
                        nuevoValor= str(input('Ingrese el nuevo valor para el id del Responsable de la Modificacion <-> '))
                        editar['idRespMov'] = nuevoValor
                    elif (op=='3'):
                        break
        ReAsig(inventario,codCampus)
    else:
        print('No has ingresado ninguna persona...')
        cf.pausar_pantalla()

def Historial(inventario, codCampus, tipo):
    inventario['activos'][codCampus]['Estado'] = tipo
    countAsigId = len(inventario['activos'][codCampus]['historialActivo'])+1
    NroId = str(countAsigId).zfill(3)
    History={
        'NroId':NroId,
        'fecha':datenow,
        'tipoMov': tipo,
        'idRespMov':input('Ingrese el id de la persona que realizo el movimiento <-> ')
    }
    inventario['activos'][codCampus]['historialActivo'].update({NroId:History})