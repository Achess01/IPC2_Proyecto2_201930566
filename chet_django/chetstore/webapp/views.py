from django.shortcuts import render

# Create your views here.
def codemirror(request):
    if request.method == 'POST'    :
        print('*'*10)
        data = request.POST['data']
        print(data)
        print('*'*10)
    return render(request, 'codemirror.html')
