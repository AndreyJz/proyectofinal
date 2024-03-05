from corefiles import pausar_pantalla, borrar_pantalla, Search, Try, SiONO
from tabulate import tabulate
from copy import deepcopy

marcas = ['Lg', 'Compumax', 'Logitech', 'Benq', 'Asus', 'Lenovo', 'Hp']
categorias = ['Equipo de computo', 'Electrodomestido', 'juego']
tipos = ['monitor', 'cpu', 'teclado', 'mouse', 'aire acondicionado', 'portatil', 'impresora']

def MCT(mct,opcion): #una funcion para resumir la seleccion de marcas/categorias/tipos
        borrar_pantalla()
        print(f'A que {opcion} pertenece el activo :')
        for idx, item in enumerate(mct):
            print(f'{idx+1}. {item}') #lista las opciones segun la lista ingresada
        isValueTrue= True
        while isValueTrue:
            try: #try para prevenir el ingreso de un no entero
                op = int(input(')_')) 
            except ValueError:
                print('no estas ingresando un numero')
                pausar_pantalla()
            else:
                if op > len(mct) or op < 1: #comprobacion de opciones
                    print('estas ingresando una opcion invalida')
                else:
                    return mct[op-1]


def AddActivo (inventario: dict):
    codTransaccion = str(input('ingrese el codigo de transaccion :'))
    nroFormulario = str(input('ingrese el numero de formulario :'))
    while True:
        codCampus = Try('str','ingrese el codigo de campus :',inventario)
        if codCampus in inventario['activos']:
            print('el activo ya existe\nsi deseas crear un activo con este codigo\nelimina el activo anterior')
            if not SiONO('deseas añadir el activo con otro codCampus? Si[S/s] NO[Enter]', 'si'):#si esto se cumple entonces se sale de la funcion para que 
                return
        else:
            break
    marca = MCT(marcas,'marca')#se llama la funcion MCT para facilitar la seleccion de marcas
    categoria = MCT(categorias,'categoria')#se llama la funcion MCT para facilitar la seleccion de categoria
    tipo = MCT(tipos,'tipo')#se llama la funcion MCT para facilitar la seleccion de tipos
    borrar_pantalla()
    valor = Try('float','Ingrese el valor unitario <-> ', inventario)
    proveedor = str(input('ingrese el proveedor'))
    nroSerial = str(input('ingrese el numero serial'))
    empResponsable = str(input('ingrese cual es la empresa responsable :'))
    Estado = 'no asignado'
    historialActivo = {}
    
    activo = {
        'codTransaccion': codTransaccion,
        'nroFormulario': nroFormulario, 
        'codCampus': codCampus,
        'marca': marca,
        'categoria': categoria,
        'tipo': tipo,
        'valor': valor,
        'proveedor': proveedor,
        'nroSerial': nroSerial,
        'empResponsable': empResponsable,
        'Estado': Estado,
        'historialActivo': historialActivo   
    }
    
    inventario['activos'].update({codCampus: activo})

def EditActivo(inventario):
    if inventario['activos']:
        print('ingresa el codigo de campus del activo que desees editar :')
        codCampus= Search(inventario, 'activos')
        isValueTrue = True
        while isValueTrue:
            borrar_pantalla()
            print('que valor deseas editar?')
            menu = '1. codTransaccion\n2. nroFormulario\n3. marca\n4. categoria\n5. tipo\n6. valor\n7. proveedor\n8. nroSerial\n9. empResponsable\n10. guardar y salir' #menu para seleccionar lo qye se va a editar
            print(menu)
            op = str(input(')_'))
            editar= inventario['activos'][codCampus] #resumiendo la ruta a editar
            if op == '1':
                nuevoValor= str(input('ingrese el codigo de transaccion :'))
                editar['codTransaccion']= nuevoValor
            elif op == '2':
                nuevoValor= str(input('ingrese el numero de formulario :'))
                editar['nroFormulario']= nuevoValor
            elif op == '3':
                nuevoValor= MCT(marcas)
                editar['marca']= nuevoValor
            elif op == '4':
                nuevoValor= MCT(categorias)
                editar['categoria']= nuevoValor
            elif op == '5':
                nuevoValor= MCT(tipos)
                editar['tipo']= nuevoValor
            elif op == '6':
                nuevoValor= tryValueError()
                editar['valor']= nuevoValor
            elif op == '7':
                nuevoValor= str(input('ingrese el proveedor'))
                editar['proveedor']= nuevoValor
            elif op == '8':
                nuevoValor= tryValueError()
                editar['nroSerial']= nuevoValor
            elif op == '9':
                nuevoValor= str(input('ingrese cual es la empresa responsable :'))
                editar['empResponsable']= nuevoValor
            elif op == '10':
                print('saliendo del menu de edicion...')
                pausar_pantalla()
                isValueTrue= False
            else:
                print('el valor que estas ingresando no es valido')
                pausar_pantalla()   
    else:
        return
        
def SearchActivo(inventario: dict): #busca activos y los imprime
    codCampus = Search(inventario, 'activos')
    inventariocopy = deepcopy(inventario)
    tabla = []
    diccionario = dict(inventariocopy['activos'][codCampus])
    del(diccionario['historialActivo'])
    tabla.append(diccionario)
    print(tabulate(tabla, headers='keys', tablefmt='grid'))
    pausar_pantalla()
