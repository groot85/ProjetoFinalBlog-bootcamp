from django.urls import path
from . import views

#home, por isso ''

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]