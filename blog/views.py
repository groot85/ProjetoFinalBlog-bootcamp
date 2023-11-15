from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# A view is a place where we put the "logic" of our application
def inicio (request):
    return render(request,'inicio.html')

def post_list (request):
    return render (request, 'post_list.html',)

#https://docs.djangoproject.com/en/3.2/ref/models/querysets/
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})