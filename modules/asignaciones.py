import corefiles as cf
from datetime import datetime

datenow = str(datetime.now())

def AddAsig(dataInventario):
        opciones = '1. Persona\n2. Zona'
        print(opciones)
        tipoAsig = cf.Try('str','Ingrese el tipo de la asignacion <-> ',dataInventario)
        isValueTrue = True
        while isValueTrue:
            if not len(dataInventario['zonas']) == 0 and len(dataInventario['personas']) == 0:
                if not len(dataInventario['personas']) == 0:
                    print('inventario vacio')
                    if tipoAsig == '1':
                        tipoAsig = 'persona'
                        for key,value in dataInventario['personas'].items():
                            print(f'{key} -- {value["nombre"]}')
                        AsignadoA = cf.Try('int','Ingrese el id de la persona que le asignara <-> ',dataInventario)
                    elif tipoAsig == '2':
                        tipoAsig= 'zona'
                        for key,value in dataInventario['zonas'].items():
                            print(f'{key} -- {value["nombreZona"]}')
                        if len(dataInventario)['zonas'] == 0:
                            print('inventario vacio')
                            if cf.SiONO('deseas cambiar el tipo de asignacion? SI(s/S) o NO(enter)', 'si'):
                                tipoAsig = '1'
                            else:
                                print('regresando al menu principal...')
                                return
                        AsignadoA = cf.Try('int','Ingrese el Nro de la zona que le asignara <-> ',dataInventario)
                    for key in dataInventario['asignacion'].keys:
                        if AsignadoA == key:
                            if cf.SiONO('esta asignacion ya existe, deseas editarla Si(S/s) o No(enter) ', 'si'):
                                existe = True
                                isValueTrue= False
                            else:
                                print('ingrese otra zona/persona')
                        else:
                            isValueTrue= False
                    else:
                        print('opcion invalida')
                else:
                    cf.borrar_pantalla()
                    print('debes ingresar al menos una persona\nregresando al menu prinipal...')
                    cf.pausar_pantalla()
                    return
            else:
                cf.borrar_pantalla()
                print('no hay activos ni personas a los que asignar\nregresando al menu principal...')
                cf.pausar_pantalla()
                return
            if existe:
                Activos = dataInventario['asignacion'][AsignadoA]['activos']
            else:
                Activos = []
            lstNotAsig=[]
            for key,value in dataInventario['activos'].items():
                    if dataInventario['activos'][key]['Estado'] == 'no asignado':
                        lstNotAsig.append(key)
                    if len(lstNotAsig) == 0:
                        print('no hay activos para asignar\nregresando al menu principal')
                        cf.pausar_pantalla()
                        return
            while True: #Ciclo para listar los Activos que no se encuentran asignados
                Activo = cf.Try('str','Ingrese el codCampus del activo que desea agregar <-> ',dataInventario)
                if Activo not in lstNotAsig: 
                    print('El valor que estas ingresando no existe o ya esta asignado...')
                    cf.pausar_pantalla()
                elif Activo in Activos:
                    print('Valor ya agregado en esta asignacion...')
                    cf.pausar_pantalla()
                else:
                    Activos.append(Activo)
                    dataInventario['activos'][Activo]['Estado'] = 'asignado'
                if not len(Activos) == len(lstNotAsig):
                    if not cf.SiONO('Desea seguir asignando Activos? S(si) o Enter(no) -> ', 'si'):
                        if len(Activos) == 0:
                            print('Debe asignar al menos un activo...')
                            cf.pausar_pantalla()
                        else:
                            break
        Asig={
            'NroAsig':NroAsig,
            'fechaAsig':datenow,
            'tipoAsig':tipoAsig,
            'asignadoA':AsignadoA,
            'activos':Activos
        }
        dataInventario.get('asignacion').update({AsignadoA:Asig})
        countAsig = len(dataInventario['activos'][Activo]['historialActivo'])+1
        NroAsig = str(countAsig).zfill(3) 
        isValueTrue= True
        while isValueTrue:
            cf.borrar_pantalla()
            for key,value in dataInventario['personas'].items():
                print(f'{key} -- {value["nombre"]}')
            idRespMov = str(input('quien fue el responsable del movimimiento :'))
            if idRespMov == dataInventario['personas'].keys():
                isValueTrue = False
            else:
                print('ingresa una id valida')
                cf.borrar_pantalla()
        History={
            'NroId':NroAsig,
            'fecha':datenow,
            'tipoMov':'asignacion',
            'idRespMov': idRespMov
        }
        dataInventario['activos'][Activo]['historialActivo'].update({NroAsig:History})

def ReturnAct(inventario):
    print('Ingrese el id del activo que quiere retornar de reparacion ')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Retornado')
 
def DardeBaja(inventario):
    print('Ingrese el id del activo que quiere dar de baja')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Dado de baja')
    for key,value in inventario['asignacion'].items():
        if codCampus in value['activos']:
            value['activos'].pop[codCampus]

def GarantiaAct(inventario):
    print('Ingrese el id del activo que quiere aplicar la garantia')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Reparacion/Garantia')

def ReAsig(inventario,codCampus):
    Historial(inventario, codCampus, 'ReAsignado')
    for key,value in inventario['asignacion'].items():
        if codCampus in value['activos']:
            value['activos'].pop[codCampus]

def ChangeAsig(inventario):
    lstNotAsig=[]
    if inventario['personas']:
        print('ingresa el Codigo del activo que desees reasignar :')
        for key,value in inventario['activos'].items():
            if (inventario['activos'][key]['Estado'] == 'asignado')or(inventario['activos'][key]['Estado'] == 'Reasignado'):
                lstNotAsig.append(key)
        codCampus = cf.Search(inventario, 'activos')
        if codCampus not in lstNotAsig: 
            print('El valor ingresado no esta en la lista mostrada...')
            cf.pausarpantalla()
        else:
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