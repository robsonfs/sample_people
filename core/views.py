from django.shortcuts import render
from django.views.generic import ListView

from core.models import People


def people_list(request):
    pessoas = People.objects.all()
    context = {
        "pessoas": pessoas
    }
    return render(request, 'core/list.html', context=context)
