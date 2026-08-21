from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):

    context = {
        'vehiculos_hoy': 0,
        'en_proceso': 0,
        'terminados': 0,
        'ingresos_hoy': 0,
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )