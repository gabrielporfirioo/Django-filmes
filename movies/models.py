from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    description = models.TextField()  # Descrição obtida pela API
    custom_description = models.TextField(blank=True)  # Descrição personalizada
    poster_url = models.URLField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Relaciona cada filme a um usuário

    
    
    def __str__(self):
        return self.title
    


