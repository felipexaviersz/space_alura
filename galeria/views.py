from django.shortcuts import render



def index(request):

    dados = {
    1: {"nome": "Nebulosa",
        "legenda": "webtelescop.org / NASA / James Webb"},
    2: {"nome": "Galaxia NGC 170",
        "legenda": "NASA.org / NASA / Hubble"}
    }


    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
