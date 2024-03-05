import corefiles as cf
from datetime import datetime
from tabulate import tabulate

datenow = str(datetime.now())

def AddAsig(dataInventario): #funcion para crear asignacion
    existe= False #variable creada para ser usada si una asignacion existe
    originalLeng = 0 #originalLeng es una variable creada para el condicional de la linea 121
    isValueTrue = True
    responsable = 0 
    while isValueTrue: #primer ciclo while para la condiccion de la linea 63
        cf.borrar_pantalla()
        opciones = '1. Persona\n2. Zona' 
        print(opciones)
        tipoAsig = cf.Try('str','Ingrese el tipo de la asignacion <-> ',dataInventario) #pregunta el tipo de asignacion (1/2)
        isValueTrue1= True
        while isValueTrue1: #segundo ciclo while para el resto de condiciones
            cf.borrar_pantalla()
            if len(dataInventario['zonas']) != 0 or len(dataInventario['personas']) != 0: #Si los diccionarios zonas/personas estan vacios, se ejecuta else
                if not len(dataInventario['personas']) == 0: #si personas esta vacio ejecuta el else (personas es necesario para el registro del historial)
                    if tipoAsig == '1': #si selecciona la opcion 1 tipoAsig se vuelve persona
                        tipoAsig = 'persona'
                        for key,value in dataInventario['personas'].items(): #ciclo for para imprimir las personas existentes
                            print(f'{key} -- {value["nombre"]}')
                        AsignadoA = cf.Try('str','Ingrese el id de la persona que le asignara <-> ',dataInventario)
                        if AsignadoA in dataInventario['personas']: #si la persona asignada no existe (se reinicia el ciclo)
                            isValueTrue1= False
                        else:
                            print('la persona ingresada no existe')
                            cf.pausar_pantalla()
                            tipoAsig= '1' #devuelve el valor a 1 para el correcto funcionamiento del codigo
                            continue
                    elif tipoAsig == '2': #si selecciona la opcion 2 tipoAsig se vuelve zona
                        tipoAsig= 'zona'
                        for key,value in dataInventario['zonas'].items(): #ciclo for para imprimir las zonas existentes
                            print(f'{key} -- {value["nombreZona"]}') 
                        if len(dataInventario['zonas']) == 0: #si no hay elementos en zonas:
                            print('inventario vacio')
                            cf.pausar_pantalla()
                            if cf.SiONO('deseas cambiar el tipo de asignacion? SI(s/S) o NO(enter)', 'si'): #da la opcion de ingresar una persona
                                tipoAsig = '1'
                            else:
                                print('regresando al menu principal...') #si no desea ingresar una persona regresa al menu principal
                                cf.pausar_pantalla()
                                return
                        AsignadoA = cf.Try('str','Ingrese el Nro de la zona que le asignara <-> ',dataInventario) 
                        if AsignadoA in dataInventario['zonas']: #si la zona asignada no existe (se reinicia el ciclo)
                            isValueTrue1= False
                        else:
                            print('la zona ingresada no existe')
                            cf.pausar_pantalla()
                            tipoAsig= '2' #devuelve el valor a 2 para el correcto funcionamiento del codigo
                    else: #si la opcion seleccionada no es 1 o 2 ejecuta else
                        print('has ingresado una opcion invalida')
                        cf.pausar_pantalla()
                        isValueTrue1= False
                    if AsignadoA in dataInventario['asignacion']: #condicional para comprobar si la asignacion a persona existe
                        if cf.SiONO('esta asignacion ya existe, deseas agregar mas activos? Si(S/s) o No(enter) ', 'si'): #si existe, pregunta si desea añadir mas activos
                            existe = True #la variable existe se vuelve verdadera si la asignacion existe 
                            isValueTrue= False
                        else: #en tal caso de que no desee reiniciar la zona se reinicia desde el primer ciclo while
                            print('ingrese otra zona/persona') 
                            cf.pausar_pantalla()
                    elif AsignadoA in dataInventario['personas'] or AsignadoA in dataInventario['zonas']: #si la asignacion no existe continua
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
    if existe: #si existe es verdadero
        Activos = dataInventario['asignacion'][AsignadoA]['activos'] #trae activos de la asignacion existente
        originalLeng = len(Activos) #se reemplaza con el largo de los activos ya existentes
    else:
        Activos = [] #activos se crea vacion si la asignacion no existe
    lstNotAsig=[] 
    for key,value in dataInventario['activos'].items(): #ciclo for creado para añadir a una lista los activos no asignados
            if dataInventario['activos'][key]['Estado'] == 'no asignado':
                lstNotAsig.append(key)
    if len(lstNotAsig) == 0: #si no hay activos para asignar sale de la funcion
        print('no hay activos para asignar\nregresando al menu principal')
        cf.pausar_pantalla()
        return
    while True: #Ciclo para listar los Activos que no se encuentran asignados
        cf.borrar_pantalla()
        Activo = cf.Try('str','Ingrese el codCampus del activo que desea agregar <-> ',dataInventario)
        if tipoAsig == 'zona': #si el tipo de asignacion es 'zona' se ejecuta
            if len(Activos) == dataInventario['zonas'][AsignadoA]['totalCapacidad']: #condicional para comprobar si la capacidad llego a su maximo
                print('Se ha igualado la capacidad maxima de la zona, no se pueden agregar mas activos')
                cf.pausar_pantalla()
                Activo = Activos[-1] #regresa al ultimo activo asignado para guardar correctamente la informacion
                break
        if Activo not in lstNotAsig:  #condicional para combrobar que el valor sea asignable
            print('El valor que estas ingresando no existe o ya esta asignado...')
            cf.pausar_pantalla()
        elif Activo in Activos: #condicional para evitar que se asigne dos veces el mismo activo
            print('Valor ya agregado en esta asignacion...')
            cf.pausar_pantalla()
        else: #se ejecuta si ninguno de los dos condicionales anteriores fue ejecutado
            Activos.append(Activo)
            dataInventario['activos'][Activo]['Estado'] = 'asignado'
            countAsig = len(dataInventario['activos'][Activo]['historialActivo'])+1
            NroId = str(countAsig).zfill(3) 
            if responsable == 0: #condicional para preguntar el responsable una sola vez
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
        if len(Activos) != len(lstNotAsig) + originalLeng: #permite ingresar asignaciones hasta que no existan mas
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
    if tipoAsig == 'persona': #asigna una letra al inicio de cada id para evitar la creacion de asignaciones con el mismo nombre
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
        print('1. Retornar de garantia\n2. Retornar asignacion\n3. Regresar al menu princial') #da la posibilidad de retornar de una asignacion o de garantia
        op = input(')_')
        if op == '1': 
            print('Ingrese el id del activo que quiere retornar de reparacion ')
            codCampus= cf.Search(inventario, 'activos')
            if inventario['activos'][codCampus]['Estado'] != 'Reparacion/Garantia': #si el activo no se encuentra en garantia no se puede retornal
                print('el activo que deseas retornar debe encontrarse en reparacion o garantia\nvolviendo al menu...')
                cf.pausar_pantalla()
                return
            else:
                Historial(inventario, codCampus, 'asignado')
        elif op=='2':
            print('Ingrese el id del activo que quiere retornar de asignacion ')
            codCampus= cf.Search(inventario, 'activos')
            for value in inventario['asignacion'].values(): #ciclo for para buscar la lista en la que se encuentra el activo
                if codCampus in value['activos']:
                    for idx, item in enumerate(value['activos']): #ciclo for para eliminar el activo
                        if codCampus == item:
                            del(value['activos'][idx])
                    break
            Historial(inventario, codCampus, 'no asignado')
        elif op=='3':
            return
        else:
            print('El valor ingresado no es valido')
            cf.pausar_pantalla()
 
def DardeBaja(inventario): #funcion para dar de baja a activo
    print('Ingrese el id del activo que quiere dar de baja')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Dado de baja')
    for key,value in inventario['asignacion'].items(): #misma funcion de la linea 162
        if codCampus in value['activos']:
            for idx, item in enumerate(value['activos']): #misma funcion de la linea 164
                if codCampus == item:
                    del(value['activos'][idx])
                    break

def GarantiaAct(inventario): #funcion para enviar activo a garantia 
    print('Ingrese el id del activo que quiere aplicar la garantia')
    codCampus= cf.Search(inventario, 'activos')
    Historial(inventario, codCampus, 'Reparacion/Garantia')

def ReAsig(inventario): #funcion para re asignar un activo
    if len(inventario['asignacion']) >= 2: #la funcion solo se ejecuta si existen dos asignaciones
        print('ingrese el activo que desea reasignar')
        codCampus= cf.Search(inventario, 'activos')
        if inventario['activos'][codCampus]['Estado'] == 'asignado' or inventario['activos'][codCampus]['Estado'] == 'ReAsignado': #comprueba que el estado del activo le permita re asignar
            print('ingresa la asignacion a la que deseas reasignar el activo\nestas son las asignaciones disponibles')
            for key in inventario['asignacion'].keys(): #ciclo for que muestra que asignaciones estan disponibles
                print(key)
            asignacionR = cf.Search(inventario, 'asignacion') 
            nuevaStr= asignacionR[1:] #quita el primer valor a zonas para la condicion de la linea 201
            if (inventario['asignacion'][asignacionR]['tipoAsig'] == 'zona') and (len(inventario['asignacion'][asignacionR]['activos'])) == (inventario['zonas'][nuevaStr]['totalCapacidad']):
                print('la zona a la que estas intentando re asignar el activo esta llena') # la funcion del condicional es no permitir añadir mas activos a una zona llena
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

def Historial(inventario, codCampus, tipo): #funcion para actualizar historial
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

def SearchAsig(inventario: dict): #funcion para buscar asignacion (en menu)
    codCampus = cf.Search(inventario, 'asignacion')
    tabla = []
    diccionario = dict(inventario['asignacion'][codCampus])
    tabla.append(diccionario)
    print(tabulate(tabla, headers='keys', tablefmt='grid'))
    cf.pausar_pantalla()