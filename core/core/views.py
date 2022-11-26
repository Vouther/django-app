from django.http import HttpResponse
import json

def home(requeste):
    response = {"msg": "Todo ok"}
    #Lo convierte en un json
    #return HttpResponse(json.dumps(response))}
    return HttpResponse("<h1>Hola desde Home</h1>")