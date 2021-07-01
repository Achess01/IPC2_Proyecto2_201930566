import csv
from io import StringIO
import re
from typing import List
import xml.etree.ElementTree as ET
import xml.dom.minidom as domxml

CL_HEADERS = set(['nombre', 'apellido', 'edad', 'fechacumpleaños', 'fechaprimeracompra'])
BCL_HEADERS = set(['nombre', 'fechaultimacompra', 'cantidadcomprada', 'cantidadgastada'])
#G_HEADERS = set(['nombre', 'plataforma', 'añoLanzamiento', 'clasificación', 'stock'])
G_HEADERS = set(['nombre', 'plataforma', 'añolanzamiento', 'clasificacion'])
MSG_HEADERS = set(['nombre', 'fechaultimacompra', 'copiasvendidas', 'stock'])
PATTERNS = {
    'nombre': '[áéíóúa-zÁÉÍÓÚA-Z]{2,}\s?[áéíóúa-zÁÉÍÓÚA-Z]{1,}',
    'edad': '\d\d',
    'fecha': '\d{1,2}\/\d{2,2}\/\d{4,4}',
    'cantidad': '\d+',
    'gastado': '[0-9]+(\.[0-9]{1,2})?',
    'año': '\d{4,4}',
    'clasificacion': '[ETM]',    
    'no_validate': '.+'
}
LIST_CL = []
LIST_BC = []
LIST_G = []
LIST_MS = []


def analize_files(files):
    LIST_CL.clear()
    LIST_BC.clear()
    LIST_G.clear()
    LIST_MS.clear()
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
        #print(new_fielnames)
        if len(set(new_fielnames) & CL_HEADERS) == len(new_fielnames) and filesFound['clients'] == None:
            filesFound['clients'] = csv_reader.reader
        elif len(set(new_fielnames) & BCL_HEADERS) == len(new_fielnames) and filesFound['best_clients'] == None:
            filesFound['best_clients'] = csv_reader.reader
        elif len(set(new_fielnames) & G_HEADERS) == len(new_fielnames) and filesFound['games'] == None:
            filesFound['games'] = csv_reader.reader
        elif len(set(new_fielnames) & MSG_HEADERS) == len(new_fielnames) and filesFound['most_selled'] == None:
            filesFound['most_selled'] = csv_reader.reader
        else:
            return None        
    return validate_fields(filesFound)            
    
def get_XML(clients, best_clients, games, most_selled):    
    clients_xml = get_nodes_XML(clients,['nombre', 'apellido', 'edad', 'fechaCumpleaños', 'fechaPrimeraCompra'], 'clientes', 'cliente')
    best_clients_xml = get_nodes_XML(best_clients,['nombre', 'fechaUltimaCompra', 'cantidadComprada', 'cantidadGastada'], 'mejoresClientes', 'mejorCliente')
    games_xml = get_nodes_XML(games,['nombre', 'plataforma', 'añoLanzamiento', 'clasificacion'], 'juegos', 'juego')
    most_selled_xml = get_nodes_XML(most_selled,['nombre', 'fechaUltimaCompra', 'copiasVendidas', 'stock'], 'juegosMasVendidos', 'juegoMasVendido')
    chet = ET.Element("Chet")
    chet.append(clients_xml)
    chet.append(best_clients_xml)
    chet.append(games_xml)
    chet.append(most_selled_xml)    
    string_xml = ET.tostring(chet,encoding="UTF-8").decode("utf-8")
    xml = domxml.parseString(string_xml)
    prettyxml = xml.toprettyxml()
    return prettyxml

def get_nodes_XML(data, tags :List, rootTag, middleTag):    
    root = ET.Element(rootTag)
    for row in data:
        i = 0        
        middle = ET.SubElement(root, middleTag)        
        for v in row:         
            new_tag = ET.SubElement(middle, tags[i])            
            new_tag.text = v
            i+=1
    return root
                
def find_match(pattern, value, line):
    if not re.fullmatch(PATTERNS[pattern], value):
        print(value, str(line+1))
        return False        
    return True

def validate(dictReader,patterns : List):       
    try:
        line = 1
        for row in dictReader:            
            i = 0
            for v in row:                     
                if not find_match(patterns[i],v,line):
                        return False                
                i+=1
            line+=1
        return True
    except:
        #guardar error como cantidad de elementos nel
        return False

def validate_clients(clients ):
    for row in clients:        
        LIST_CL.append(row)
    return validate(LIST_CL, ['nombre', 'nombre', 'edad', 'fecha', 'fecha'])    

def validate_best_clients(best_clients ):
    for row in best_clients:
        LIST_BC.append(row)
    return validate(LIST_BC, ['nombre', 'fecha', 'cantidad', 'gastado'])

def validate_games(games):
    for row in games:
        LIST_G.append(row)
    return validate(LIST_G, ['no_validate', 'no_validate', 'año', 'clasificacion'])

def validate_most_selled(most_selled ):
    for row in most_selled:
        LIST_MS.append(row)
    return validate(LIST_MS, ['no_validate', 'fecha', 'cantidad', 'cantidad'])

def validate_fields(data):
    clients = data['clients']
    best_clients = data['best_clients']
    games = data['games']
    most_selled = data['most_selled']    
    if validate_clients(clients) and validate_best_clients(best_clients) and validate_games(games) and validate_most_selled(most_selled):                    
        return get_XML(LIST_CL, LIST_BC, LIST_G, LIST_MS)
    return None