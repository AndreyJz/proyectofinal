from corefiles import checkFile

inventario = {
    'activos': {},
    'personas': {},
    'zonas': {},
    'asignacion': {}
}
data = checkFile('data.json', inventario)

if __name__ == '__main__':
    pass