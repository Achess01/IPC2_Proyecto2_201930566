from django.shortcuts import render
from django.http.response import HttpResponse
import xml.etree.ElementTree as ET
import requests

# Create your views here.
def codemirror(request):
    if request.method == 'POST'    :
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