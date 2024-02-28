from corefiles import pausar_pantalla, borrar_pantalla, SearchActivos

marcas = ['Lg', 'Compumax', 'Logitech', 'Benq', 'Asus', 'Lenovo', 'Hp']
categorias = ['Equipo de computo', 'Electrodomestido', 'juego']
tipos = ['monitor', 'cpu', 'teclado', 'mouse', 'aire acondicionado', 'portatil', 'impresora']

def MCT(mct): #una funcion para resumir la seleccion de marcas/categorias/tipos
        borrar_pantalla()
        print('A que categoria pertenece el activo :')
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

def tryValueError():
    isValueTrue = True
    while isValueTrue:
        try:
            variable = float(input('ingrese el valor unitario'))
        except ValueError:
            print('estas ingresando un valor erroneo')
            pausar_pantalla()
        else:
            return variable
            isValueTrue = False

def AddActivo (inventario: dict):
    codTransaccion = str(input('ingrese el codigo de transaccion :'))
    nroFormulario = str(input('ingrese el numero de formulario :'))
    codCampus = str(input('ingrese el codigo de campus :'))
    marca = MCT(marcas)
    categoria = MCT(categorias)
    tipo = MCT(tipos)
    borrar_pantalla()
    valor = tryValueError()
    proveedor = str(input('ingrese el proveedor'))
    nroSerial = tryValueError()
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
        codCampus= SearchActivos(inventario, 'activos')
        isValueTrue = True
        while isValueTrue:
            borrar_pantalla()
            print('que valor deseas editar?')
            menu = '1. codTransaccion\n2. nroFormulario\n3. marca\n4. categoria\n5. tipo\n6. valor\n7. proveedor\n8. nroSerial\n9. empResponsable\n10. guardar y salir'
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
        

def DeleteActivo(inventario: dict):
    if inventario['activos']:
        borrar_pantalla()
        print('ingrese el codigo de campus del activo que desea borrar')
        codCampus= SearchActivos(inventario, 'activos')
        del(inventario['activos'][codCampus])
        print('el activo ha sido eliminado correctamente')
        pausar_pantalla()
    else:
        return
    