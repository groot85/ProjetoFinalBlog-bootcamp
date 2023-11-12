from django.shortcuts import render
from django.http import HttpResponse

# A view is a place where we put the "logic" of our application
def inicio (request):
    return render(request,'inicio.html')

def post_list (request):
    return render (request, 'post_list.html')