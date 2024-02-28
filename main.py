from corefiles import checkFile, updateData
from modules.menus import mainmenu
from externo.csv_import import AddActivoFromCampus
inventario = {
    'activos': {},
    'personas': {},
    'zonas': {},
    'asignacion': {}
}
data = checkFile('data.json', inventario)
AddActivoFromCampus(inventario)
updateData('data.json', inventario)

if __name__ == '__main__':
    mainmenu(data)