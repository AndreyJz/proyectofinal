from corefiles import borrar_pantalla, pausar_pantalla, Search
from tabulate import tabulate

def ListarActivos(inventario: dict):
    Activos = []
    inventarioNotHistorial= {}
    for key, item in inventario['activos'].items():
        inventarioNotHistorial.update({key: item})
        try:
            del inventarioNotHistorial[key]['historialActivo'] #borramos la key historial, para evitar fallos en tabulate
        except KeyError:
            continue
    for key, item in inventarioNotHistorial.items():
        Activos.append(item) #se ingresan los valores en una tabla para que tabulate cree una sola lista
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        borrar_pantalla()
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        pausar_pantalla()
        
def ListarCategoria(inventario: dict):
    Activos = []
    inventarioNotHistorial= {}
    categorias = ['Equipo de computo', 'Electrodomestido', 'juego']
    print('que categoria deseas buscar?')
    for idx, item in enumerate(categorias):
        print(f'{idx+1}. {item}')
    isValueTrue= True
    while isValueTrue:
        op= str(input('ingrese una opcion (numero) :'))
        if op == '1':
            categoria= 'Equipo de computo'
            isValueTrue = False
        elif op == '2':
            categoria= 'Electrodomestido'
            isValueTrue = False
        elif op == '3':
            categoria=  'juego'
            isValueTrue = False
        else:
            print('opcion invalida :C')
            pausar_pantalla()
    for key, item in inventario['activos'].items():
        inventarioNotHistorial.update({key: item})
        try:
            del inventarioNotHistorial[key]['historialActivo'] 
        except KeyError:
            continue
    for key, item in inventarioNotHistorial.items():
        if inventarioNotHistorial[key]['categoria'] == categoria: 
            Activos.append(item) 
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        borrar_pantalla()
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        pausar_pantalla()

def listarDadoDeBajo(inventario):
    Activos = []
    inventarioNotHistorial= {}
    for key, item in inventario['activos'].items():
        inventarioNotHistorial.update({key: item})
        try:
            del inventarioNotHistorial[key]['historialActivo'] 
        except KeyError:
            continue
    for key, item in inventarioNotHistorial.items():
        if inventarioNotHistorial[key]['Estado'] == 'Dado de baja':
            Activos.append(item) 
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        borrar_pantalla()
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        pausar_pantalla()

def listarRepYAct(inventario = dict):
    pass

def ListarActivoHist(inventario: dict):
    historialActivo = []
    print('ingresa el codCampus del que desees ver el historial')
    codCampus = Search(inventario, 'activos')
    for key, values in inventario['activos'][codCampus]['historialActivo'].items():
        historialActivo.append(values)
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(historialActivo), lines_per_page)):
        subset_data = historialActivo[i:i + lines_per_page]
        totalPag = len(historialActivo)//lines_per_page
        borrar_pantalla()
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx + 1} de {totalPag + 1}')
        pausar_pantalla()