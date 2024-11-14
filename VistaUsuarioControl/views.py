from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import HttpRequest
from .models import Estudiante,Curso,AsignacionDocenteCurso,AsignacionEstudianteCurso,Docente
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
# Create your views here.
def Menu_Principal(request):
    return render(request,'Paginas/index.html')



def Camara(request):
    if request.method == "POST":
        data = json.loads(request.body)
        carnet = data.get('codigo_qr')
        try:
            # Busca el estudiante que tenga el carnet proporcionado
            usuario = Estudiante.objects.get(Carnet=carnet)
            # Devuelve la información del estudiante como respuesta JSON
            return JsonResponse({
                'encontrado': True,
                'estudiante': {
                    'NombreEstudiante': usuario.NombreEstudiante,
                    'Carnet': usuario.Carnet,
                    'Imagen': usuario.Imagen.url if usuario.Imagen else '',
                }
            })
        except Estudiante.DoesNotExist:
            return JsonResponse({'encontrado': False})

    return render(request, 'Paginas/camara.html')

