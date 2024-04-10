from django.http import HttpResponse 
import os 

def saludar(request):
    mensaje= "Hola mundo, esto es un mensaje"
    return HttpResponse(mensaje)
      

def apagar(request): 
    os.system("Shutdonw -s -t 3600")
    return HttpResponse("El equipo se apagara en 3600 segundos")