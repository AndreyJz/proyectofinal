from tabulate import tabulate
from corefiles import borrar_pantalla, pausar_pantalla, updateData, delOp, Search
import modules.Activos as act
import modules.reportes as rep
import modules.asignaciones as a
import modules.personas as p
import modules.zonas as z
import os


def mainmenu(data): #menu principal
    borrar_pantalla()
    global inventario
    inventario = data
    
    issAppRunning = True
    while issAppRunning:
        borrar_pantalla()
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
            opcion='personas'
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
            print('Gracias por usar el programa, vuelva pronto!')
            pausar_pantalla()
            issAppRunning= False
        else:
            print('El valor ingresado no esta asociado a una seccion...')
            pausar_pantalla()
            mainmenu(data)

def menuAPZ(opcion): #menu (agregar contenido)
    borrar_pantalla()
    opTitulo = str(opcion).upper()
    titulo = f"""
    +++++++++++++++++
    [ MENU {opTitulo} ]
    +++++++++++++++++
    """
    print(titulo)
    opciones = '1. Agregar\n2. Editar\n3. Eliminar\n4. Buscar\n5. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op=='1'):
        borrar_pantalla()
        if opcion == 'activos':
            act.AddActivo(inventario)
            updateData('data.json', inventario)
        elif opcion == 'personas':
            p.AddPersona(inventario)
            updateData('data.json', inventario)
        elif opcion == 'zonas':
            z.AddZona(inventario)
            updateData('data.json', inventario)
    elif (op=='2'):
        borrar_pantalla()
        if opcion == 'activos':
            act.EditActivo(inventario)
            updateData('data.json', inventario)
        elif opcion == 'personas':
            p.EditPersona(inventario)
            updateData('data.json', inventario)
        elif opcion == 'zonas':
            z.EditZona(inventario)
            updateData('data.json', inventario)
    elif (op=='3'):
        borrar_pantalla()
        abc= {}
        if opcion == 'zonas':
            abc.update(sorted(inventario['zonas'].items())) 
            for key, value in abc.items():
                print(f'{key}. {value["nombreZona"]}')
        delOp(inventario,opcion)
    elif (op=='4'):
        borrar_pantalla()
        if inventario[opcion]:
            if opcion == 'activos':
                print('Ingrese el numero de identificacion del activo a buscar <-> ')
                act.SearchActivo(inventario)
            elif opcion == 'personal':
                print('Ingrese el numero de identificacion de la persona a buscar <-> ')
                p.SearchPpl(inventario)
            elif opcion == 'zonas':
                print('Ingrese el numero de identificacion de la zona a buscar <-> ')
                z.SearchZone(inventario)
        else:
            print(f'no has ingresado ningun valor en {opcion}')
            pausar_pantalla()
    elif (op=='5'):
        borrar_pantalla()
        print('Volviendo al menu principal...')
        pausar_pantalla()
        mainmenu(inventario)
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        pausar_pantalla()
        menuAPZ(opcion)


    
def menuAsigActivos(): #menu de asignacion de activos
    borrar_pantalla()
    titulo = """
    ++++++++++++++++++++++++++++++
    [ MENU ASIGNACION DE ACTIVOS ]
    ++++++++++++++++++++++++++++++
    """
    print(titulo)
    opciones = '1. Crear Asignacion\n2. Buscar Asignacion\n3. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op=='1'):
        borrar_pantalla()
        a.AddAsig(inventario)
        updateData('data.json', inventario)
    elif(op=='2'):
        borrar_pantalla()
        print('Ingrese el numero de identificacion de la persona o zona que se asigno en la asignacion <-> ')
        a.SearchAsig(inventario)
    elif(op=='3'):
        borrar_pantalla()
        print('Volviendo al menu principal...')
        pausar_pantalla()
        mainmenu(inventario)
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        pausar_pantalla()
        menuAsigActivos()

def menuRep(): #menu de reportes
    borrar_pantalla()
    titulo = """
    +++++++++++++++++
    [ MENU REPORTES ]
    +++++++++++++++++
    """
    print(titulo)
    opciones = '1. Lista Activos\n2. Lista Activos por Categoria\n3. Lista Activos dados de Baja\n4. Lista Activos y Asignacion\n5. Lista Historial de Mov. de Activo\n6. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op=='1'):
        borrar_pantalla()
        rep.ListarActivos(inventario)
    elif (op=='2'):
        borrar_pantalla()
        rep.ListarCategoria(inventario)
    elif (op=='3'):
        borrar_pantalla()
        rep.listarDadoDeBajo(inventario)
    elif (op=='4'):
        borrar_pantalla()
        rep.listarRepYAct(inventario)
    elif (op=='5'):
        borrar_pantalla()
        rep.ListarActivoHist(inventario)
    elif (op=='6'):
        borrar_pantalla()
        print('Volviendo al menu principal...')
        os.system('pause')
        mainmenu(inventario)
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        pausar_pantalla()
        menuRep()

def menuMOVActivos():  #menu de movimiento de activos
    borrar_pantalla()
    titulo = """
    ++++++++++++++++++++++++++++++
    [ MENU MOVIMIENTO DE ACTIVOS ]
    ++++++++++++++++++++++++++++++
    """
    print(titulo)
    opciones = '1. Retorno de activo\n2. Dar de Baja Activo\n3. Cambiar Asignacion de Activo\n4. Envia a Garantia Activo\n5. Regresar al Menu Principal\n'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')
    if (op=='1'):
        borrar_pantalla()
        a.ReturnAct(inventario)
        updateData('data.json', inventario)
    elif(op=='2'):
        borrar_pantalla()
        a.DardeBaja(inventario)
        updateData('data.json', inventario)
    elif(op=='3'):
        borrar_pantalla()
        a.ReAsig(inventario)
        updateData('data.json', inventario)
    elif(op=='4'):
        borrar_pantalla()
        a.GarantiaAct(inventario)
        updateData('data.json', inventario)
    elif(op=='5'):
        borrar_pantalla()
        print('Volviendo al menu principal...')
        pausar_pantalla()
        mainmenu()
    else:
        print('El valor ingresado no esta asociado a una seccion...')
        pausar_pantalla() 
        menuMOVActivos()
        