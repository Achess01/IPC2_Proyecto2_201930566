
import xml.etree.cElementTree as ET
from datetime import datetime

FILENAME = 'data.xml'
def add_data(data):
    try:
        xml = ET.parse(FILENAME)
        root = xml.getroot()     
        clients = root.find('clientes')   
        games = root.find('juegos')               
        cla_E = games.find("clasificacionCuenta/[@value='E']")
        cla_T = games.find("clasificacionCuenta/[@value='T']")
        cla_M = games.find("clasificacionCuenta/[@value='M']")
    except:
        xml = ET.ElementTree(ET.Element("Chet"))
        root = xml.getroot()
        clients = ET.SubElement(root, "clientes")        
        games = ET.SubElement(root, "juegos")                             
        cla_E = ET.SubElement(games, 'clasificacionCuenta')
        cla_T = ET.SubElement(games, 'clasificacionCuenta')
        cla_M = ET.SubElement(games, 'clasificacionCuenta')
        cla_E.set('value', 'E')
        cla_T.set('value', 'T')
        cla_M.set('value', 'M')
        cla_E.text = "0"
        cla_T.text = "0"
        cla_M.text = "0"
            
    # clients = root.find("clientes/cliente")    
    # print(clients)       
    
    try:
        new = ET.fromstring(data)
    except:        
        parseData = data.decode('Latin-1')
        new = ET.fromstring(parseData)
    
    clients_list = new.findall('clientes/cliente')
    best_clients_list = new.findall('mejoresClientes/mejorCliente')    
    for client in clients_list:        
        new_client = ET.SubElement(clients, "cliente")
        name = ET.SubElement(new_client, "nombre")
        name.text = client.find('nombre').text +" " + client.find('apellido').text
        age = ET.SubElement(new_client, "edad") 
        age.text = client.find('edad').text
        birthday = ET.SubElement(new_client, "fechaCumpleaños")
        birthday.text = client.find('fechaCumpleaños').text
        first_buy = ET.SubElement(new_client, "fechaPrimeraCompra")
        first_buy.text = client.find('fechaPrimeraCompra').text
        is_best = new.find("mejoresClientes/mejorCliente/[nombre='"+name.text+"']")
        lb = "-"
        am = "0"
        ex = "0"
        if is_best != None:
            lb = is_best.find('fechaUltimaCompra').text
            am = is_best.find('cantidadComprada').text
            ex = is_best.find('cantidadGastada').text
            best_clients_list.remove(is_best)
        last_buy = ET.SubElement(new_client, 'fechaUltimaCompra')
        last_buy.text = lb
        amount = ET.SubElement(new_client, "cantidadComprada")
        amount.text = am
        expensed = ET.SubElement(new_client, 'cantidadGastada')
        expensed.text = ex        

    for client in best_clients_list:        
        new_client = ET.SubElement(clients, "cliente")
        name = ET.SubElement(new_client, "nombre")
        name.text = client.find('nombre').text
        age = ET.SubElement(new_client, "edad") 
        age.text = "-"
        birthday = ET.SubElement(new_client, "fechaCumpleaños")
        birthday.text = "-"
        first_buy = ET.SubElement(new_client, "fechaPrimeraCompra")
        first_buy.text = "-"                
        last_buy = ET.SubElement(new_client, 'fechaUltimaCompra')
        last_buy.text = client.find('fechaUltimaCompra').text
        amount = ET.SubElement(new_client, "cantidadComprada")
        amount.text = client.find('cantidadComprada').text
        expensed = ET.SubElement(new_client, 'cantidadGastada')
        expensed.text = client.find('cantidadGastada').text        
        
    games_list = new.findall('juegos/juego')    
    most_selled_games_list = new.findall('juegosMasVendidos/juegoMasVendido')
    count_E = 0
    count_T = 0
    count_M = 0
    for game in games_list:                
        new_game = ET.SubElement(games, "juego")
        name = ET.SubElement(new_game,"nombre")
        name.text = game.find('nombre').text
        platform = ET.SubElement(new_game, "plataforma")
        platform.text = game.find('plataforma').text
        release_year = ET.SubElement(new_game, 'añoLanzamiento')
        release_year.text = game.find('añoLanzamiento').text
        classification = ET.SubElement(new_game, 'clasificacion')
        classification.text = game.find('clasificacion').text
        if classification.text == 'E':
            count_E+=1
        elif classification.text == 'T':
            count_T+=1
        elif classification.text == 'M':
            count_M+=1
        last_buy = ET.SubElement(new_game, 'fechaUltimaCompra')
        copies_selled = ET.SubElement(new_game, 'copiasVendidas')
        stock = ET.SubElement(new_game, 'stock')
        is_most_selled = new.find('juegosMasVendidos/juegoMasVendido/[nombre="'+name.text+'"]')
        lb = "-"
        nc = "0"
        st = game.find('stock').text
        if is_most_selled != None:
            lb = is_most_selled.find('fechaUltimaCompra').text
            nc = is_most_selled.find('copiasVendidas').text
            st = is_most_selled.find('stock').text
            most_selled_games_list.remove(is_most_selled)
        last_buy.text = lb
        copies_selled.text = nc
        stock.text = st
        color = ET.SubElement(new_game, "color")
        color_text = "#000"
        if int(st) < 10:
            color_text = "#F00"
        color.text = color_text

    for game in most_selled_games_list:
        new_game = ET.SubElement(games, "juego")
        name = ET.SubElement(new_game,"nombre")
        name.text = game.find('nombre').text
        platform = ET.SubElement(new_game, "plataforma")
        platform.text = "-"
        release_year = ET.SubElement(new_game, 'añoLanzamiento')
        release_year.text = "-"
        classification = ET.SubElement(new_game, 'clasificacion')
        classification.text = "-"
        last_buy = ET.SubElement(new_game, 'fechaUltimaCompra')
        copies_selled = ET.SubElement(new_game, 'copiasVendidas')
        stock = ET.SubElement(new_game, 'stock')                            
        last_buy.text = game.find('fechaUltimaCompra').text
        copies_selled.text = game.find('copiasVendidas').text
        stock.text = game.find('stock').text
        color = ET.SubElement(new_game, "color")
        color_text = "#000"
        if int(stock.text) < 10:
            color_text = "#F00"
        color.text = color_text

        
    cla_E.text = str(int(cla_E.text)+ count_E)
    cla_T.text = str(int(cla_T.text)+ count_T)
    cla_M.text = str(int(cla_M.text)+ count_M)
        
    xml.write(FILENAME, encoding='UTF-8', xml_declaration=True)

def get_best_clients():
    try:
        xml = ET.parse(FILENAME)    
        root = xml.getroot()
        bests = root.findall("clientes/cliente")
        bests = [client for client in bests if client.find('cantidadGastada').text != '0']
        bests.sort(key=lambda client: float(client.find('cantidadGastada').text), reverse=True)
        response = ET.ElementTree(ET.Element("mejoresClientes"))
        response_root = response.getroot()
        for client in bests:
            response_root.append(client)        
        return ET.tostring(response_root, encoding='UTF-8')
    except ValueError as e:   
        print(e)             
        response = ET.Element("Message")
        response.text = "No se encontraron datos"
        return ET.tostring(response, encoding='UTF-8')
    
def get_best_games():
    try:
        xml = ET.parse(FILENAME)    
        root = xml.getroot()
        bests = root.findall("juegos/juego")
        bests = [game for game in bests if game.find('copiasVendidas').text != '0']
        bests.sort(key=lambda game: int(game.find('copiasVendidas').text), reverse=True)
        response = ET.ElementTree(ET.Element("juegosMasVendidos"))
        response_root = response.getroot()
        for game in bests:
            response_root.append(game)        
        return ET.tostring(response_root, encoding='UTF-8')
    except:        
        response = ET.Element("Message")
        response.text = "No se encontraron datos"
        return ET.tostring(response, encoding='UTF-8')

def get_games_classification():
    try:
        xml = ET.parse(FILENAME)    
        root = xml.getroot()
        cla = root.findall("juegos/clasificacionCuenta")        
        cla.sort(key=lambda classification: int(classification.text), reverse=True)
        response = ET.ElementTree(ET.Element("clasificacionJuegos"))
        response_root = response.getroot()
        for classification in cla:
            response_root.append(classification)        
        return ET.tostring(response_root, encoding='UTF-8')
    except:        
        response = ET.Element("Message")
        response.text = "No se encontraron datos"
        return ET.tostring(response, encoding='UTF-8')


def get_day_month(strdate):
    actual_year = datetime.today().year    
    date = datetime.strptime(strdate, "%d/%m/%Y")    
    return datetime.date(datetime(actual_year, date.month, date.day))
    
def get_birthdays():
    try:
        xml = ET.parse(FILENAME)    
        root = xml.getroot()
        birthdays = root.findall("clientes/cliente")        
        birthdays = [birthday for birthday in birthdays if birthday.find('fechaCumpleaños').text != '-']
        birthdays.sort(key=lambda birthday: get_day_month(birthday.find('fechaCumpleaños').text))
        response = ET.ElementTree(ET.Element("cumpleaños"))
        response_root = response.getroot()
        for classification in birthdays:
            cl = classification.find('fechaCumpleaños')
            date = datetime.strptime(cl.text, "%d/%m/%Y")
            date = date.strftime('%d/%B')
            cl.text = str(date)
            response_root.append(classification)        
        return ET.tostring(response_root, encoding='UTF-8')
    except:        
        response = ET.Element("Message")
        response.text = "No se encontraron datos"
        return ET.tostring(response, encoding='UTF-8')

def get_games():
    try:
        xml = ET.parse(FILENAME)    
        root = xml.getroot()
        games = root.findall("juegos/juego")        
        games.sort(key=lambda game: int(game.find('stock').text), reverse=True)
        response = ET.ElementTree(ET.Element("juegos"))
        response_root = response.getroot()
        for game in games:
            response_root.append(game)        
        return ET.tostring(response_root, encoding='UTF-8')
    except:        
        response = ET.Element("Message")
        response.text = "No se encontraron datos"
        return ET.tostring(response, encoding='UTF-8')
