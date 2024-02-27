import os

def mainmenu():
    titulo = """
    +++++++++++++++++++++++++++++++++++++++++
    [ SISTEMA G&C DE INVENTARIO CAMPUSLANDS ]
    +++++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3,4,5,6,7]
    opciones = '1. Activos\n2. Personal\n3. Zonas\n4. Asignacion de activos\n5. Reportes\n6. Movimiento De Activos\n7. Salir'
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
        print('Gracias por usar el programa, vuelva pronto! :D')
        os.system('pause')
    else:
        print('El valor ingresado no esta asociado a unaa seccion...')
        os.system('pause')
        mainmenu()

def menuAPZ(opcion):
    titulo = f"""
    +++++++++++++++++
    + MENU {opcion} +
    +++++++++++++++++
    """
    print(titulo)
    lstOp=[1,2,3,4,5]
    opciones = '1. Agregar\n2. Editar\n3. Eliminar\n4. Buscar\n5. Salir'
    print(opciones)
    op = input('Ingrese el numero de la seccion a la que quiere ingresar <-> ')