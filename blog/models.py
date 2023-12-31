from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0,'rascunho'),(1, 'publicado'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) #texto do titulo, caracteres limitados
    slug = models.SlugField(max_length=40,default=slugify(title)) #criar url personalizada do post, sem ID publica
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #login par publicacao e regra de exclusao dos dados ao excluir autor
    created_date = models.DateTimeField(auto_now_add=True) #data e hora conforme tiemzone
    update_on = models.DateField(auto_now =True)
    content = models.TextField() #texto do blog, texto longo, caracteres ilimitados
    status = models.IntegerField(choices=STATUS, default=0) #padrao do post é rascunho
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date'] 

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
    return self.title
        
    