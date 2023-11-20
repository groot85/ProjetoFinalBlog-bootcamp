from . import views
from django.urls import path

#home, por isso ''
urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
  
]