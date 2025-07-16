from django.shortcuts import render

def lista_frutas(request):
    frutas = ['Maçã', 'Banana', 'Laranja', 'Abacaxi', 'Manga']
    return render(request, 'lista_frutas.html', {'frutas': frutas})
