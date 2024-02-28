from csv import reader

def AddActivoFromCampus(inventario = dict):
    data = []
    with open('externo/activos.csv', 'r') as activos:
        lector = reader(activos, delimiter=';')
        for row in lector:
            elementos = row[0].split(',')
            data.append(elementos)
        for item in data:
            activoCampus= {
            'codTransaccion': item[0],
            'nroFormulario': item[1], 
            'codCampus': item[2],
            'marca': item[3],
            'categoria': item[4],
            'tipo': item[5],
            'valor': item[6],
            'proveedor': item[7],
            'nroSerial': item[8],
            'empResponsable': item[9],
            'Estado': item[10],
            'historialActivo': {}  
            }
            inventario['activos'].update({activoCampus['codCampus']: activoCampus})