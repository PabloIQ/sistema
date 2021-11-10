from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from core.models import Modelo, Marca, TipoDispositivo, TipoCaso, Caso
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def Index(request):
    caso = Caso.objects.all()
    return render(request, 'caso/ver.html', {
        'caso': caso
    })

@login_required(login_url='login')
def CrearCaso(request):
    dispositivo = TipoDispositivo.objects.values('id', 'nombre')
    marca_list = Marca.objects.values('id', 'nombre')
    modelo_list = Modelo.objects.values('id', 'nombre')
    caso_tipo = TipoCaso.objects.values('id', 'nombre')
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        tipo_dispositivo = request.POST['tipo_dispositivo']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        tipo_caso = request.POST['tipo_caso']
        cliente = request.POST['cliente']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        estado = request.POST['estado']
        recibido = request.POST['recibido']
        entregado = request.POST['entregado']
        monto = request.POST['monto']

        caso = Caso(
            descripcion = descripcion,
            id_tipo_dispositivo = TipoDispositivo.objects.get(id=tipo_dispositivo),
            id_marca = Marca.objects.get(id=marca),
            id_modelo = Modelo.objects.get(id=modelo),
            id_tipo_caso = TipoCaso.objects.get(id=tipo_caso),
            nombre_cliente = cliente,
            telefono_cliente = telefono,
            direccion_cliente = direccion,
            estado_caso = estado,
            fecha_recibido = recibido,
            fecha_entregado = entregado,
            monto = monto
        )
        caso.save()
        messages.success(request, 'Caso creada registrada correctamente')
    return render(request, 'caso/crear.html', {
        'dispositivo': dispositivo,
        'marca': marca_list,
        'modelo': modelo_list,
        'caso_tipo': caso_tipo
    })

@login_required(login_url='login')
def CasoDetalle(request, id):
    #lista = ['Mi texto']
    caso = Caso.objects.get(id=id)
    #print('CAso id: ', caso.id)
    #print(request)
    #lista.append(caso.id + ' mi texto')
    return JsonResponse({
        'desc': caso.descripcion,
        'dispositivo': caso.id_tipo_dispositivo.nombre,
        'marca': caso.id_marca.nombre,
        'modelo': caso.id_modelo.nombre,
        'caso': caso.id_tipo_caso.nombre
        })

@login_required(login_url='login')
def CrearTipoCaso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            tipo_caso = TipoCaso(
                nombre = nombre
            )
            tipo_caso.save()
            messages.success(request, 'Se ha creado correctamente el tipo de caso!')
        except:
            messages.error(request, 'Hubo un error al crear el tipo de caso!!!!')
    return render(request, 'caso/crear_tipo.html')

@login_required(login_url='login')
def CrearTipoDispositivo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            dispositivo = TipoDispositivo(
                nombre = nombre
            )
            dispositivo.save()
            messages.success(request, 'El tipo de dispositivo se creado correctamente!')
        except:
            messages.error(request, 'Hubo un error al crear el tipo de dispositivo!!')
    return render(request, 'dispositivo/crear_tipo.html')

@login_required(login_url='login')
def CrearMarca(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            marca = Marca(
                nombre= nombre
            )
            marca.save()
            messages.success(request, 'La marca se ha creado correctamente!')
        except:
            messages.error(request, 'Hubo un error al crear la marca')
    return render(request, 'marca/crear.html')

@login_required(login_url='login')
def CrearModelo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            modelo = Modelo(
                nombre = nombre
            )
            modelo.save()
            messages.success(request, 'El modelo se creado correctamente!')
        except:
            messages.error(request, 'Hubo un error al crear el modelo')
    return render(request, 'modelo/crear.html')

def Login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {request.user}!!')
            return redirect('index')
        else:
            messages.error(request, 'Usuario inválido, vuelve a intentarlo!!')

    return render(request, 'login/login.html')

def Logout(request):
    user = request.user
    logout(request)
    messages.success(request, f'Vuelva pronto {user}!!!')
    return redirect('login')    

def Guardar(request, estado, fecha, monto, id):
    caso = Caso.objects.get(id=id)
    caso.estado_caso = estado
    caso.fecha_entregado = fecha
    caso.monto = monto
    caso.save()
    messages.success(request, 'Se aplicaron los cambios!')
    return redirect('index')

def Eliminar(request, id):
    caso = Caso.objects.get(id=id)
    caso.delete()
    messages.success(request, 'Se eliminado un elemento en la lista!!')
    return redirect('index')