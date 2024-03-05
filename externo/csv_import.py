from csv import reader

def AddActivoFromCampus(inventario: dict):
    data = []
    with open('externo/activos.csv', 'r') as activos: #abre en lectura el csv
        lector = reader(activos, delimiter=';') #separa las lines del csv por medio de;
        for row in lector: #itera sobre cada fila
            elementos = row[0].split(',') #parte cada elemento de la lista por medio de la coma
            data.append(elementos)
        for item in data:
            valor = float(item[6]) #convierte en float el valor
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
            'historialActivo': {}  
            }
            inventario['activos'].update({activoCampus['codCampus']: activoCampus})