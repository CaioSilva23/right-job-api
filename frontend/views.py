from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from api.models import Tecnologia

def home(request):
    tecnologias = get_list_or_404(Tecnologia)
    return render(request, 'frontend.html', {'tecnologias': tecnologias})