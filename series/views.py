from django.shortcuts import render
from .models import Publicacion  # Asegurate de que Publicacion esté bien importado

def lista_series(request):
    # Obtiene todas las publicaciones ordenadas por fecha de publicación descendente
    publicaciones = Publicacion.objects.order_by('-fecha_publicacion')

    return render(request, 'lista_series.html', {
        'publicaciones': publicaciones
    })
