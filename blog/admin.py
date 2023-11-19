from django.contrib import admin
from .models import Post

#class PostAdmin (admin.ModelAdmin): 

admin.site.register(Post)