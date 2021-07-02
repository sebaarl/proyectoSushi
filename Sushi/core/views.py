from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from core.forms import CustomUserFrom, ProductoForm, TipoForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from AppProductos.models import Producto, Tipo
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def menu(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/menu.html', data)

def contact(request):
    return render(request, 'core/contact.html')

def apirest(request):
    return render(request, 'core/api.html')

def registro_usuario(request):
    data = {
        'form' : CustomUserFrom()
    }

    if request.method == 'POST':
        formulario = CustomUserFrom(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)

def grupo_usuario(user):
    return user.is_superuser or user.groups.filter(name='Vendedor').exists() or user.groups.filter(name='Supervisor').exists()

@user_passes_test(grupo_usuario)
def staffUsers(request):
    return render(request, 'core/staff.html')

@user_passes_test(grupo_usuario)
def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/listado_productos.html', data)

@user_passes_test(grupo_usuario)
def listado_tipos(request):
    tipos = Tipo.objects.all()
    data = {
        'tipos': tipos
    }
    return render(request, 'core/listado_tipos.html', data)

@permission_required('AppProductos.add_producto')
def nuevo_producto(request):
    data = {
        'form': ProductoForm()        
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Producto guardado exitosamente!'

    return render(request, 'core/nuevo_producto.html', data)

@permission_required('AppProductos.add_tipo')
def nuevo_tipo(request):
    data = {
        'form': TipoForm()    
    }

    if request.method == 'POST':
        formulario = TipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Tipo agregado exitosamente!'

    return render(request, 'core/nuevo_tipo.html', data)

@permission_required('AppProductos.change_producto')
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Producto modificado correctamente!'
            data['form'] = formulario
    
    return render(request, 'core/modificar_producto.html', data)

@permission_required('AppProductos.change_tipo')
def modificar_tipo(request, id):
    tipo = Tipo.objects.get(id=id)
    data = {
        'form' : TipoForm(instance=tipo)
    }

    if request.method == 'POST':
        formulario = TipoForm(data=request.POST, instance=tipo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Tipo modificado correctamente!'
            data['form'] = formulario
    
    return render(request, 'core/modificar_tipo.html', data)

@permission_required('AppProductos.delete_tipo')
def eliminar_tipo(request, id):
    tipo = Tipo.objects.get(id=id)
    tipo.delete()

    return redirect(to='listado_tipos')

@permission_required('AppProductos.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to='listado_productos')

def superuser(user):
    return user.is_superuser

@user_passes_test(superuser)
def listado_usuarios(request):
    usuario = User.objects.all()
    data = {
        'usuarios' : usuario 
    }

    return render(request, 'core/listado_usuarios.html', data)

@user_passes_test(superuser)
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()

    return redirect(to='listado_usuarios')

@user_passes_test(superuser)
def modificar_usuario(request, id ):
    usuario = User.objects.get(id=id)
    data = {
        'form' : CustomUserFrom(instance=usuario)
    }

    if request.method == 'POST':
        formulario = CustomUserFrom(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'El usuario ha modificado correctamente!'
            data['form'] = formulario

    return render(request, 'core/modificar_usuario.html', data)