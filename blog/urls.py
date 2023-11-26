from django.urls import path
from . import views
#from .views import SearchResultsView

#home, por isso ''
urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    #path('search/', views.SearchResultsView.as_view(), name= 'search_results')
    path('search_results/', views.search, name='search'),
 
   
]   