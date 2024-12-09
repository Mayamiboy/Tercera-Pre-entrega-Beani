from django.shortcuts import render, HttpResponse
from datetime import datetime
from .forms import AuthorForm  # Importar AuthorForm
from .models import Author  # Asegúrate de tener esto si usas el modelo Author

def dia_de_hoy(request):
    dia = datetime.now().strftime("%Y-%m-%d")
    documento_de_texto = f"Hoy es: <br> {dia}"
    return HttpResponse(documento_de_texto)

def mi_nombre(request, nombre):
    return HttpResponse(f"Mi nombre es: {nombre} // Genio programador de coderhouse pero por falta de tiempo y mucho laburo no alcanza a completar las entregas")

def home(request):
    return render(request, 'templatetop.html')

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def search_author(request):
    if request.method == "GET" and 'q' in request.GET:
        query = request.GET['q']
        results = Author.objects.filter(name__icontains(query)) # type: ignore
    else:
        results = []
    return render(request, 'search_author.html', {'results': results})

def saludo(request):
    return render(request, 'saludo.html')
