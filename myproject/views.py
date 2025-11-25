from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur mon projet Django !")
