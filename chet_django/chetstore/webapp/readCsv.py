import csv
from io import StringIO

CL_HEADERS = set(['nombre', 'apellido', 'edad', 'fechaCumpleaños', 'fechaPrimeraCompra'])
BCL_HEADERS = set(['nombre', 'fechaUltimaCompra', 'cantidadComprada', 'cantidadGastada'])
#G_HEADERS = set(['nombre', 'plataforma', 'añoLanzamiento', 'clasificación', 'stock'])
G_HEADERS = set(['nombre', 'plataforma', 'añoLanzamiento', 'clasificación'])
MSG_HEADERS = set(['nombre', 'fechaUltimaCompra', 'copiasVendidas'])


def analize_files(files):
    filesFound = {
        'clients': None,
        'best_clients': None,
        'games': None,
        'most_selled': None
    }
    for file in files:                         
        content = StringIO(file.read().decode('utf-8'))
        csv_reader = csv.DictReader(content, delimiter=';')                                                  
        new_fielnames = list(map(lambda header: header.lower(),csv_reader.fieldnames))                
        csv_reader.fieldnames = new_fielnames 
        print(new_fielnames)
        if 'nombre' in csv_reader:
            print(csv_reader['nombre'])
        if len(set(new_fielnames) & CL_HEADERS) == len(new_fielnames) and filesFound['clients'] == None:
            filesFound['clients'] = csv_reader
        elif len(set(new_fielnames) & BCL_HEADERS) == len(new_fielnames) and filesFound['best_clients'] == None:
            filesFound['best_clients'] = csv_reader
        elif len(set(new_fielnames) & G_HEADERS) == len(new_fielnames) and filesFound['games'] == None:
            filesFound['games'] = csv_reader
        elif len(set(new_fielnames) & MSG_HEADERS) == len(new_fielnames) and filesFound['most_selled'] == None:
            filesFound['most_selled'] = csv_reader
        else:
            return None
    return filesFound

def validate_field(data : csv.DictReader):
    pass