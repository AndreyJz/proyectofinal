from modules.Activos import AddActivo, EditActivo, DeleteActivo
from corefiles import borrar_pantalla, pausar_pantalla, updateData
import os


def mainmenu(data): #menu principal
    borrar_pantalla()
    
    global inventario
    inventario = data
    
    issAppRunning = True
    while issAppRunning:
        titulo = """
        +++++++++++++++++++++++++++++++++++++++++
        [ SISTEMA G&C DE INVENTARIO CAMPUSLANDS ]
        +++++++++++++++++++++++++++++++++++++++++
        """
        print(titulo)
        opciones = '1. Activos\n2. Personal\n3. Zonas\n4. Asignacion de activos\n5. Reportes\n6. Movimiento De Activos\n7. Salir'
        print(opciones)
        op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
        if (op=='1'):
            opcion='activos'
            menuAPZ(opcion)
        elif (op=='2'):
            opcion='personal'
            menuAPZ(opcion)
        elif (op=='3'):
            opcion='zonas'
            menuAPZ(opcion)
        elif (op=='4'):
            menuAsigActivos()
        elif (op=='5'):
            menuRep()
        elif (op=='6'):
            menuMOVActivos()
        elif (op=='7'):
            print('Gracias por usar el programa, vuelva pronto! :D')
            os.system('pause')
            issAppRunning= False
        else:
            print('El valor ingresado no esta asociado a una seccion...')
            os.system('pause')
            mainmenu(data)

def menuAPZ(opcion): #menu (agregar contenido)
    titulo = f"""
    +++++++++++++++++
    [ MENU {opcion} ]
    +++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3,4,5]
    opciones = '1. Agregar\n2. Editar\n3. Eliminar\n4. Buscar\n5. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op=='1'):
        if opcion == 'activos':
            AddActivo(inventario)
            updateData('data.json', inventario)
        elif opcion == 'personal':
            pass
        elif opcion == 'zonas':
            pass
    elif (op=='2'):
        if opcion == 'activos':
            EditActivo(inventario)
            updateData('data.json', inventario)
        elif opcion == 'personal':
            pass
        elif opcion == 'zonas':
            pass
    elif (op=='3'):
        if opcion == 'activos':
            DeleteActivo(inventario)
            updateData('data.json', inventario)
        elif opcion == 'personal':
            pass
        elif opcion == 'zonas':
            pass
    elif (op=='4'):
        if opcion == 'activos':
            pass
        elif opcion == 'personal':
            pass
        elif opcion == 'zonas':
            pass
    elif (op=='5'):
        print('Volviendo al menu principal...')
        os.system('pause')
        mainmenu(inventario)
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        os.system('pause')
        menuAPZ(opcion)


    
def menuAsigActivos(): #menu de asignacion de activos
    titulo = """
    ++++++++++++++++++++++++++++++
    [ MENU ASIGNACION DE ACTIVOS ]
    ++++++++++++++++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3]
    opciones = '1. Crear Asignacion\n2. Buscar Asignacion\n3. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op==1):
        pass
    elif(op==2):
        pass
    elif(op==3):
        print('Volviendo al menu principal...')
        os.system('pause')
        mainmenu()
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        os.system('pause')
        menuAsigActivos()

def menuRep(): #menu de reportes
    titulo = """
    +++++++++++++++++
    [ MENU REPORTES ]
    +++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3,4,5,6,7]
    opciones = '1. Lista Activos\n2. Lista Activos por Categoria\n3. Lista Activos dados de Baja\n4. Lista Activos y Asignacion\n5. Lista Historial de Mov. de Activo\n6. Movimiento De Activos\n7. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op==1):
        pass
    elif (op==2):
        pass
    elif (op==3):
        pass
    elif (op==4):
        pass
    elif (op==5):
        pass
    elif (op==6):
        pass
    elif (op==7):
        print('Volviendo al menu principal...')
        os.system('pause')
        mainmenu()
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        os.system('pause')
        menuRep()

def menuMOVActivos():  #menu de movimiento de activos
    titulo = """
    ++++++++++++++++++++++++++++++
    [ MENU MOVIMIENTO DE ACTIVOS ]
    ++++++++++++++++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3,4,5]
    opciones = '1. Retorno de activo\n2. Dar de Baja Activo\n3. Cambiar Asignacion de Activo\n4. Envia a Garantia Activo\n5. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op==1):
        pass
    elif(op==2):
        pass
    elif(op==3):
        pass
    elif(op==4):
        pass
    elif(op==5):
        print('Volviendo al menu principal...')
        os.system('pause')
        mainmenu()
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        os.system('pause')   
        menuMOVActivos()
        