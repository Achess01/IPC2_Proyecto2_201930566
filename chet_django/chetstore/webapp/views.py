from typing import IO
from django.shortcuts import render
from django.http.response import HttpResponse
import xml.etree.ElementTree as ET
import requests
from webapp.readCsv import analize_files

# Create your views here.

##Subir archivo

def getData(request):
    response = {
        'messageError': '',
        'messageSucces': '',
        'validator': False,
    }
    if request.method == 'POST':   
        if 'data' in request.POST:
            data = request.POST['data']
            response['messageSucces'] = "Datos guardados"
            print(data)
        elif len(request.FILES.getlist('subir')) == 4:   
            analized = analize_files(request.FILES.getlist('subir'))                 
            if  analized == None:                
                response['validator'] = False
                response['messageError'] = "Uno de los archivos tiene el formato incorrecto"
            else:
                print(analized)
                response['validator'] = True
                response['messageSucces'] = "BUENA"
        else:
            response['messageError'] = "Error: Tiene que subir exactamente 4 archivos"
    return render(request, 'getData.html', response)
## Requests

def see_requests(request):
    return render(request, 'requests.html')

def codemirror(request):
    if request.method == 'POST':
        print('*'*10)        
        data = request.POST['data']
        print(data)
        print('*'*10)                    
    return render(request, 'codemirror.html')            

def most_selled(request):
    try:
        r = requests.get('http://127.0.0.1:4000/most_selled')    
        if r.status_code == 200:
            response = ET.fromstring(r.text)
            games = response.findall('juego')
            labels = list(map(lambda game: game.find('nombre').text + " " + game.find('añoLanzamiento').text, games))
            data = list(map(lambda game: int(game.find('copiasVendidas').text), games))        
        data_graph = {
            'labels': labels,
            'data': data
        }    
        return render(request, 'mostSelled.html', data_graph)
    except:
        return HttpResponse('Verifique que la api esté disponible')

def best_clients(request):
    try:
        r = requests.get('http://127.0.0.1:4000/best_clients')    
        if r.status_code == 200:
            response = ET.fromstring(r.text)
            clients = response.findall('cliente')
            labels = list(map(lambda client: client.find('nombre').text, clients))
            data = list(map(lambda client: int(client.find('cantidadGastada').text), clients))        
        data_graph = {
            'labels': labels,
            'data': data
        }    
        return render(request, 'bestClients.html', data_graph)
    except:
        return HttpResponse('Verifique que la api esté disponible')

def games_classification(request):
    try:
        r = requests.get('http://127.0.0.1:4000/games_classification')    
        if r.status_code == 200:
            response = ET.fromstring(r.text)
            games_classification = response.findall('clasificacionCuenta')
            labels = list(map(lambda classification: classification.attrib['value'], games_classification))
            data = list(map(lambda classification: int(classification.text), games_classification))        
        data_graph = {
            'labels': labels,
            'data': data
        }    
        return render(request, 'gamesClassification.html', data_graph)
    except:
        return HttpResponse('Verifique que la api esté disponible')
    
def birthdays(request):
    try:
        r = requests.get('http://127.0.0.1:4000/birthdays')    
        if r.status_code == 200:
            response = ET.fromstring(r.text)
            birthdays = response.findall('cliente')
            clients = []
            for client in birthdays:
                new_client = {
                    'name': client.find('nombre').text,
                    'birthday': client.find('fechaCumpleaños').text,
                    'first_buy': client.find('fechaPrimeraCompra').text
                }
                clients.append(new_client)            
        data_birthdays = {
            'clients': clients
        }    
        return render(request, 'birthdays.html', data_birthdays)
    except:
        return HttpResponse('Verifique que la api esté disponible')

def games(request):
    try:
        r = requests.get('http://127.0.0.1:4000/games')    
        if r.status_code == 200:
            response = ET.fromstring(r.text)
            games = response.findall('juego')
            games_list = []
            for game in games:                                
                new_game = {
                    'name': game.find('nombre').text,
                    'platform': game.find('plataforma').text,
                    'release': game.find('añoLanzamiento').text,
                    'cla': game.find('clasificacion').text,
                    'selled': game.find('copiasVendidas').text,
                    'stock': game.find('stock').text,
                    'color': game.find('color').text
                }
                games_list.append(new_game)            
        data_games = {
            'games': games_list
        }    
        return render(request, 'games.html', data_games)
    except:
        return HttpResponse('Verifique que la api esté disponible')