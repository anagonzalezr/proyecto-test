from django.shortcuts import redirect, render
from .models import Producto, Usuario
from .forms import ProductoForm, RegistroForm, ContactoGeneralForm

# Create your views here.


def index(request):
    context     = {}
    productos   = Producto.objects.all() # muestro todos los productos
    context     = {
                    'productos'     : productos 
                  }
    return render(request, 'ground_zero/index.html', context)


def listaProductos(request):
    productos   = Producto.objects.all() # muestro todos los productos
    context     = {
                    'productos'     : productos 
                  }
    return render(request, 'ground_zero/listaProductos.html', context) # para direccionar a la pagina


def agregarProductos(request):
    context     = {
                    'form'          : ProductoForm() # de donde extraigo el formulario
                  }
    if request.method=='POST': # traigo los campos 'POST'
        formulario = ProductoForm(request.POST, files=request.FILES) # recupero los datos subidos | el files sirve para recuperar imagenes
        if formulario.is_valid: # valido el formulario
            formulario.save()
            context={
                        'mensaje'   : "¡Producto Correctamente Agregado!"
                    }  
    return render(request, 'ground_zero/agregarProductos.html', context)


def editarProductos(request, pk):
    producto    = Producto.objects.get(id_producto = pk) # busco el producto por su id cuando el id seleccionado sea igual al del producto
    context     = {
                    'form'          : ProductoForm(instance=producto)
                  }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto) # llamo a los datos | indico que selecciono
        if formulario.is_valid: 
            formulario.save()
            context={
                        'mensaje'   : "¡Producto Actualizado!"
                    } 
    return render(request, 'ground_zero/editarProductos.html', context)


def eliminarProductos(request, pk):
    producto    = Producto.objects.get(id_producto = pk)
    producto.delete()
    return redirect(to='listaProductos') # re dirigo a la lista para ver los cambios


def registrarUsuario(request):
    context     = {
                    'form'          : RegistroForm()
                  }
    if request.method=='POST': 
        formulario = RegistroForm(request.POST) 
        if formulario.is_valid:
            formulario.save()
            context={
                        'mensaje'   : "¡Usuario Registrado!"
                    }
    return render(request, 'ground_zero/registrarUsuario.html', context)


def ingresoUsuario(request):
    context     = {
                    'form'          : RegistroForm()
                  }
    if request.method=='POST': 
        formulario = RegistroForm(request.POST) 
        if formulario.is_valid:
            formulario.check()
            context={
                        'mensaje'   : "¡Usuario Ingresado!"
                    }
    return render(request, 'ground_zero/ingresoUsuario.html', context)


def contactoGeneral(request):
    context     = {
                    'form'          : ContactoGeneralForm()
                  }
    if request.method=='POST':
        formulario = ContactoGeneralForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            context={
                        'mensaje'   : "¡Formulario Subido!"
            }
    return render(request, 'ground_zero/contactoGeneral.html', context)