from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = ((0,'rascunho'),(1, 'publicado'))

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #login par publicacao e regra de exclusao dos dados ao excluir autor
    title = models.CharField(max_length=200) #texto do titulo, caracteres limitados
    text = models.TextField() #texto do blog, texto longo, caracteres ilimitados
    created_date = models.DateTimeField(default=timezone.now) #data e hora
    status = models.IntegerField(choices=STATUS, default=0) #padrao do post é rascunho

    class Meta:
        ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title