from django.contrib import admin

from .models import Post

class PostAdmin (admin.ModelAdmin):
    list_display = ('title','slug', 'status', 'created_date')
    list_filter = ('status',)
    search_field = ('title', 'content',)

admin.site.register(Post, PostAdmin)