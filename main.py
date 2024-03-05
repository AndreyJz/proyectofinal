from corefiles import checkFile, updateData, pausar_pantalla, borrar_pantalla
from modules.menus import mainmenu
from externo.csv_import import AddActivoFromCampus
inventario = {
    'activos': {},
    'personas': {},
    'zonas': {},
    'asignacion': {}
}
data = checkFile('data.json', inventario)
#AddActivoFromCampus(inventario)
#updateData('data.json', inventario)

if __name__ == '__main__':
    while True:
        try:
            mainmenu(data)
        except KeyboardInterrupt:
            borrar_pantalla()
            print('No intente romper el codigo...')
            pausar_pantalla()
        else:
            mainmenu(data)
            break