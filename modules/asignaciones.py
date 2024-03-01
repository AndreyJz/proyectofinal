import corefiles as cf
from corefiles import Try
from datetime import datetime

datenow = str(datetime.now())

countAsg = 0

def AddAsig(dataInventario):
    countAsg += 1
    NroAsig = str(countAsig).zfill(3)
    opciones = '1. Persona\n2. Zona'
    print(opciones)
    tipoAsig = Try('str','Ingrese el tipo de la asignacion <-> ',dataInventario)
    if tipoAsig == 'personas':
        for key,value in dataInventario['personas'].items():
            print(f'{key} -- {value["nombre"]}')
        AsignadoA = Try('int','Ingrese el id de la persona que le asignara <-> ',dataInventario)
    elif tipoAsig == 'zonas':
        for key,value in dataInventario['zonas'].items():
            print(f'{key} -- {value["nombreZona"]}')
        AsignadoA = Try('int','Ingrese el Nro de la zona que le asignara <-> ',dataInventario)
    Activos = []
    lstNotAsig=[]
    while True: #Ciclo para listar los Activos que no se encuentran asignados
        for key,value in dataInventario['activos'].items():
            if dataInventario['activos'][key]['Estado'] == 'no asignado':
                lstNotAsig.append(key)
        Activo = Try('int','Estos son los Activos que no se encuentran asigados seleccione uno ingresando el id <-> ',dataInventario)
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
        'fechaAsig':datenow,
        'tipoAsig':tipoAsig,
        'asignadoA':AsignadoA,
        'activos':Activos
    }
    dataInventario.get('asignacion').update({NroAsig:Asig})
    countAsig = len(dataInventario['activos']['historialActivo'])+1
    NroAsig = str(countAsig).zfill(3) 
    History={
        'NroId':NroAsig,
        'fecha':datenow,
        'tipoMov':'asignacion',
        'idRespMov':Try('int','Ingrese el id de la persona que realizo el movimiento <-> ',dataInventario)
    }
    dataInventario['activos'][Activo]['historialActivo'].update({NroAsig:History})

def ReturnAct(inventario):
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Retornado')
 
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
                        tipoAsig = input('Ingrese el tipo de la asignacion <-> ') #!!!!!!!!!!!!!!!
                        if tipoAsig == 'personas':
                            for key,value in inventario['personas'].items():
                                print(f'{key} -- {value["nombre"]}')
                            nuevoValor = Try('int','Ingrese el id de la persona que le asignara <-> ',inventario,'')
                        elif tipoAsig == 'zonas':
                            for key,value in inventario['zonas'].items():
                                print(f'{key} -- {value["nombreZona"]}')
                            nuevoValor = Try('int','Ingrese el Nro de la zona que le asignara <-> ',inventario,'')
#editado el tipo
                        editar['tipoMov'] = nuevoValor

                    elif (op=='2'):
                        nuevoValor= Try('int','Ingrese el nuevo valor para el id del Responsable de la Modificacion <-> ',inventario,'')
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