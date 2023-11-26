from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.views import generic    

#publicacao com resumo da postagem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'

#publicacao com toda posta  gem (ler mais em: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
class DetailView (generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def search(request):
  context = {}
  query = ""
  if request.GET:
    query = request.GET.get('q', '')
    context['query'] = str(query)
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    context['posts'] = posts
  return render(request, 'search', context)


"""
class SearchResultsView(generic.DetailView):
    model = Post
    template_name = 'search_results.html'
    
    def get_queryset(self):
        return Post.objects.filter(Q(title__icontains=" "))
"""
