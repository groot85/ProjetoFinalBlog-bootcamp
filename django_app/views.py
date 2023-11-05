from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá mundo, testando a visu do Django nesse domingão de sol!</h1>")
