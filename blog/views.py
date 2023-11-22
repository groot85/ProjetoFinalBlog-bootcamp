from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views import generic

#publicacao com resumo da postagem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'

#publicacao com toda postagem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class DetailView (generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def post_list():
    return render ('','post_detail.html')

"""#https://docs.djangoproject.com/en/3.2/ref/models/querysets/
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
# A view is a place where we put the "logic" of our application
def inicio (request):
    return render(request,'index.html')
    
    
    """
