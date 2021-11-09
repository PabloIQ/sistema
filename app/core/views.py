from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from core.models import Modelo, Marca, TipoDispositivo, TipoCaso, Caso
from django.contrib import messages


# Create your views here.
def Index(request):
    caso = Caso.objects.all()
    return render(request, 'caso/ver.html', {
        'caso': caso
    })

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

    return render(request, 'caso/crear.html', {
        'dispositivo': dispositivo,
        'marca': marca_list,
        'modelo': modelo_list,
        'caso_tipo': caso_tipo
    })

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