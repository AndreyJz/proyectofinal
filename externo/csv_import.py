from csv import reader
from datetime import datetime

fechaActual = str(datetime.now())

def AddActivoFromCampus(inventario: dict):
    data = []
    with open('externo/activos.csv', 'r') as activos:
        lector = reader(activos, delimiter=';')
        for row in lector:
            elementos = row[0].split(',')
            data.append(elementos)
        for idx, item in enumerate(data):
            valor = float(item[6])
            activoCampus= {
            'codTransaccion': item[0],
            'nroFormulario': item[1], 
            'codCampus': item[2],
            'marca': item[3],
            'categoria': item[4],
            'tipo': item[5],
            'valor': valor,
            'proveedor': item[7],
            'nombre': item[8],
            'nroSerial': item[9],
            'empResponsable': item[10],
            'Estado': item[11],
            'historialActivo': {
                'Nrold': '001',
                'fecha': fechaActual,
                'tipoMOv': 'asignacion',
                'idRespMOv': ''
                }  
            }
            nroAsig = str(idx).zfill(3)
            AsignacionCampus = {
                'nroAsignacion':  nroAsig,
                'fechaAsignacion': fechaActual,
                'tipoAsignacion': 'zona',
                'asignadoA': item[12],
                'activo': item[2]
            }
            inventario['activos'].update({activoCampus['codCampus']: activoCampus})
            inventario['asignacion'].update({nroAsig: AsignacionCampus})