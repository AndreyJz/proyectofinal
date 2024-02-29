from corefiles import borrar_pantalla, pausar_pantalla
from tabulate import tabulate

def ListarActivos(inventario= dict):
    Activos = []
    inventarioNotHistorial= {}
    for key, item in inventario['activos'].items():
         inventarioNotHistorial.update({key: item})
         del inventarioNotHistorial[key]['historialActivo'] #borramos la key historial, para evitar fallos en tabulate
    for key, item in inventarioNotHistorial.items():
        Activos.append(item) #se ingresan los valores en una tabla para que tabulate cree una sola lista
    lines_per_page = 20
    for idx, i in enumerate(range(0, len(Activos), lines_per_page)):
        subset_data = Activos[i:i + lines_per_page]
        totalPag = len(Activos)//lines_per_page
        borrar_pantalla()
        print(tabulate(subset_data, headers="keys", tablefmt="grid", floatfmt=(".0f")))
        print(f'pagina {idx} de {totalPag}')
        pausar_pantalla()