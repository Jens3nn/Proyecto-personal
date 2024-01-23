from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola mundo, estás en el polls index.')
