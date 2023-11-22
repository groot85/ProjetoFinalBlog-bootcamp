from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views import generic
from django.db.models import Q

#publicacao com resumo da postagem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'

#publicacao com toda postagem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class DetailView (generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def search(request):
  context = {}
  query = ""
  if request.GET:
    query = request.GET.get('q', '')
    context['query'] = str(query)
    posts = Post.objects.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query)).distinct()
    context['posts'] = posts
  return render(request, 'search.html', context)


