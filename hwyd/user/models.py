from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField(null=False, max_length=254)
  nickname = models.CharField(max_length=255)
  
  def __str__(self):
    return f"{self.nickname}"
