from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario, Cliente
from .forms import ClienteForm
from django.shortcuts import render, redirect

#def home(request):
#    usuarios = Usuario.objects.all()
#    return render(request, "home.html", {"usuarios": usuarios})

# views.py
def home(request):
    print("Entrando en la vista home")
    if request.method == 'POST':
        print("Recibiendo una solicitud POST")
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print("Cliente creado:", form.cleaned_data)
            return redirect('home')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    print("Clientes existentes:", clientes)
    return render(request, "home.html", {"form": form, "clientes": clientes})




def prueba(request):
    return render(request, 'prueba.html')



