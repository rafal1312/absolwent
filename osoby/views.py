from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj w Django!")

def about(request):
    return HttpResponse("Informacje o aplikacji")