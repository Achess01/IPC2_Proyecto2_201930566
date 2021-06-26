from xml.etree.ElementTree import XMLParser
import xml.etree.cElementTree as ET
from xml.dom import minidom

def add_data(data):
    try:
        xml = ET.parse('data.xml')
        root = xml.getroot()     
        clients = root.find('clientes')   
        games = root.find('juegos')   
    except:
        xml = ET.ElementTree(ET.Element("Chet"))
        root = xml.getroot()
        clients = ET.SubElement(root, "clientes")        
        games = ET.SubElement(root, "juegos")        
            
    # clients = root.find("clientes/cliente")    
    # print(clients)
    new = ET.fromstring(data)
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
        last_buy = ET.SubElement(new_game, 'fechaUltimaCompra')
        copies_selled = ET.SubElement(new_game, 'copiasVendidas')
        stock = ET.SubElement(new_game, 'stock')
        is_most_selled = new.find("juegosMasVendidos/juegoMasVendido/[nombre='"+name.text+"']")
        lb = "-"
        nc = "0"
        st = "0"
        if is_most_selled != None:
            lb = is_most_selled.find('fechaUltimaCompra').text
            nc = is_most_selled.find('copiasVendidas').text
            st = is_most_selled.find('stock').text
            most_selled_games_list.remove(is_most_selled)
        last_buy.text = lb
        copies_selled.text = nc
        stock.text = st

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
        
    xml.write('data.xml', encoding='UTF-8', xml_declaration=True)


    


    
    # a = ET.ElementTree(new)
    # a.write('a.xml', encoding='UTF-8', xml_declaration=True)
    # print(new.find('clientes/cliente/fechaCumpleaños').text)
    # clients  = new.findall('clientes/cliente')    
    # cl = root.find('clientes').append(clients[7])    
    # xml.write('data.xml',encoding='UTF-8', xml_declaration=True)


    # print(new)
    # chet = data.getElementsByTagName("cliente")        
    # for cliente in chet:
    #     for datos in cliente.childNodes:
    #         if datos.nodeName != "#text":
    #             print(datos.firstChild.data)
    #xml.write('data.xml')        