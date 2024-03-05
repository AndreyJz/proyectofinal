import corefiles as cf
from datetime import datetime
from tabulate import tabulate

datenow = str(datetime.now())

def AddAsig(dataInventario):
    existe= False
    originalLeng = 0
    isValueTrue = True
    responsable = 0
    while isValueTrue:
        cf.borrar_pantalla()
        opciones = '1. Persona\n2. Zona'
        print(opciones)
        tipoAsig = cf.Try('str','Ingrese el tipo de la asignacion <-> ',dataInventario)
        isValueTrue1= True
        while isValueTrue1:
            cf.borrar_pantalla()
            if len(dataInventario['zonas']) != 0 or len(dataInventario['personas']) != 0: #Si los diccionarios zonas/personas estan vacios, se ejecuta else
                if not len(dataInventario['personas']) == 0: #si personas esta vacio ejecuta el else (personas es necesario para el registro del historial)
                    if tipoAsig == '1':
                        tipoAsig = 'persona'
                        for key,value in dataInventario['personas'].items():
                            print(f'{key} -- {value["nombre"]}')
                        AsignadoA = cf.Try('str','Ingrese el id de la persona que le asignara <-> ',dataInventario)
                        if AsignadoA in dataInventario['personas']:
                            isValueTrue1= False
                        else:
                            print('la persona ingresada no existe')
                            cf.pausar_pantalla()
                            tipoAsig= '1'
                            continue
                    elif tipoAsig == '2':
                        tipoAsig= 'zona'
                        for key,value in dataInventario['zonas'].items():
                            print(f'{key} -- {value["nombreZona"]}')
                        if len(dataInventario['zonas']) == 0:
                            print('inventario vacio')
                            cf.pausar_pantalla()
                            if cf.SiONO('deseas cambiar el tipo de asignacion? SI(s/S) o NO(enter)', 'si'):
                                tipoAsig = '1'
                            else:
                                print('regresando al menu principal...')
                                cf.pausar_pantalla()
                                return
                        AsignadoA = cf.Try('str','Ingrese el Nro de la zona que le asignara <-> ',dataInventario)
                        if AsignadoA in dataInventario['zonas']:
                            isValueTrue1= False
                        else:
                            print('la zona ingresada no existe')
                            cf.pausar_pantalla()
                            tipoAsig= '2'
                    else:
                        print('has ingresado una opcion invalida')
                        cf.pausar_pantalla()
                        isValueTrue1= False
                    if AsignadoA in dataInventario['asignacion']:
                        if cf.SiONO('esta asignacion ya existe, deseas agregar mas activos? Si(S/s) o No(enter) ', 'si'):
                            existe = True
                            isValueTrue= False
                        else:
                            print('ingrese otra zona/persona')
                            cf.pausar_pantalla()
                    elif AsignadoA in dataInventario['personas'] or AsignadoA in dataInventario['zonas']:
                        isValueTrue= False
                else:
                    cf.borrar_pantalla()
                    print('debes ingresar al menos una persona\nregresando al menu prinipal...')
                    cf.pausar_pantalla()
                    return
            else:
                cf.borrar_pantalla()
                print('no hay zonas ni personas a los que asignar\nregresando al menu principal...')
                cf.pausar_pantalla()
                return
    if existe:
        Activos = dataInventario['asignacion'][AsignadoA]['activos']
        originalLeng = len(Activos)
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
        cf.borrar_pantalla()
        Activo = cf.Try('str','Ingrese el codCampus del activo que desea agregar <-> ',dataInventario)
        
        
        if tipoAsig == 'zona':
            if len(Activos) == dataInventario['zonas'][AsignadoA]['totalCapacidad']:
                print('Se ha igualado la capacidad maxima de la zona, no se pueden agregar mas activos')
                cf.pausar_pantalla()
                Activo = Activos[-1]
                break
            
        if Activo not in lstNotAsig: 
            print('El valor que estas ingresando no existe o ya esta asignado...')
            cf.pausar_pantalla()
        elif Activo in Activos:
            print('Valor ya agregado en esta asignacion...')
            cf.pausar_pantalla()
        else:
            Activos.append(Activo)
            dataInventario['activos'][Activo]['Estado'] = 'asignado'
            countAsig = len(dataInventario['activos'][Activo]['historialActivo'])+1
            NroId = str(countAsig).zfill(3) 
            if responsable == 0:
                responsable = 1
                print('Ingrese el id del responsable de la asignacion ')
                idRespMov = cf.Search(dataInventario, 'personas')
            History={
                'NroId':NroId,
                'fecha':datenow,
                'tipoMov':'asignacion',
                'idRespMov': idRespMov
            }
            dataInventario['activos'][Activo]['historialActivo'].update({NroId:History})
        if len(Activos) != len(lstNotAsig) + originalLeng:
            if not cf.SiONO('Desea seguir asignando Activos? S(si) o Enter(no) -> ', 'si'):
                if len(Activos) == 0:
                    print('Debe asignar al menos un activo...')
                    cf.pausar_pantalla()
                else:
                    break
        else:
            print('no hay mas activos para ingresar')
            cf.pausar_pantalla()
            break
    if tipoAsig == 'persona':
        NroAsig = 'P' + AsignadoA
    else:
        NroAsig = 'Z' + AsignadoA
    Asig={
        'NroAsig':NroAsig,
        'fechaAsig':datenow,
        'tipoAsig':tipoAsig,
        'asignadoA':AsignadoA,
        'activos':Activos
    }
    dataInventario.get('asignacion').update({NroAsig:Asig})
    

def ReturnAct(inventario):
    while True:   
        print('1. Retornar de garantia\n2. Retornar asignacion\n3. Regresar al menu princial')
        op = input(')_')
        if op == '1':
            print('Ingrese el id del activo que quiere retornar de reparacion ')
            codCampus= cf.Search(inventario, 'activos')
            if inventario['activos'][codCampus]['Estado'] != 'Reparacion/Garantia':
                print('el activo que deseas retornar debe encontrarse en reparacion o garantia\nvolviendo al menu...')
                cf.pausar_pantalla()
            else:
                Historial(inventario, codCampus, 'asignado')
        elif op=='2':
            print('Ingrese el id del activo que quiere retornar de asignacion ')
            codCampus= cf.Search(inventario, 'activos')
            for value in inventario['asignacion'].values():
                if codCampus in value['activos']:
                    for idx, item in enumerate(value['activos']):
                        if codCampus == item:
                            del(value['activos'][idx])
                    break
            Historial(inventario, codCampus, 'no asignado')
        elif op=='3':
            return
        else:
            print('El valor ingresado no es valido')
            cf.pausar_pantalla()
    print('Ingrese el id del activo que quiere retornar de reparacion ')
    codCampus= cf.Search(inventario, 'activos')
    if inventario['activos'][codCampus]['Estado'] != 'Reparacion/Garantia':
        print('el activo que deseas retornar debe encontrarse en reparacion o garantia\nvolviendo al menu...')
        cf.pausar_pantalla()
        return
    Historial(inventario, codCampus, 'asignado')
    return
 
def DardeBaja(inventario):
    print('Ingrese el id del activo que quiere dar de baja')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Dado de baja')
    for key,value in inventario['asignacion'].items():
        if codCampus in value['activos']:
            for idx, item in enumerate(value['activos']):
                if codCampus == item:
                    del(value['activos'][idx])
                    break

def GarantiaAct(inventario):
    print('Ingrese el id del activo que quiere aplicar la garantia')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Reparacion/Garantia')

def ReAsig(inventario):
    if len(inventario['asignacion']) >= 2:
        print('ingrese el activo que desea reasignar')
        codCampus= cf.Search(inventario, 'activos')
        if inventario['activos'][codCampus]['Estado'] == 'asignado' or inventario['activos'][codCampus]['Estado'] == 'ReAsignado':
            print('ingresa la asignacion a la que deseas reasignar el activo\nestas son las asignaciones disponibles')
            for key in inventario['asignacion'].keys():
                print(key)
            asignacionR = cf.Search(inventario, 'asignacion')
            nuevaStr= asignacionR[1:]
            if (inventario['asignacion'][asignacionR]['tipoAsig'] == 'zona') and (len(inventario['asignacion'][asignacionR]['activos'])) == (inventario['zonas'][nuevaStr]['totalCapacidad']):
                print('la zona a la que estas intentando re asignar el activo esta llena')
                return
            inventario['asignacion'][asignacionR]['activos'].append(codCampus)
            for key,value in inventario['asignacion'].items():
                if codCampus in value['activos']:
                    for idx, item in enumerate(value['activos']):
                        if codCampus == item:
                            del(value['activos'][idx])
                    break
            Historial(inventario, codCampus, 'ReAsignado')
        else:
            print('el activo que quieres reasignar no debe estar en reparacion o dado de baja\nRegresando al menu principal...')
            cf.pausar_pantalla()
            return
    else:
        print('para reasignar un activo es necesario la existencia de al menos dos asignaciones\nRegresando al menu principal...')
        cf.pausar_pantalla()
        return

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

def SearchAsig(inventario: dict):
    codCampus = cf.Search(inventario, 'asignacion')
    tabla = []
    diccionario = dict(inventario['asignacion'][codCampus])
    tabla.append(diccionario)
    print(tabulate(tabla, headers='keys', tablefmt='grid'))
    cf.pausar_pantalla()