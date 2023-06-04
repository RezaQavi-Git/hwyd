from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField(null=False, max_length=254)
  nickname = models.CharField(max_length=255)
  password = models.CharField(max_length=2515)
  list_of_feelings = models.ManyToManyField('FeelRate')

  
  def __str__(self):
    return f"{self.nickname}"

  def get_password(self):
     return self.password
  
  def get_nickname(self):
     return self.nickname

  def check_password(self, password):
     return self.get_password() == password

class FeelRate(models.Model):
    rate = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)
    # You can add other attributes as needed

    def __str__(self):
        return f'Rate: {self.rate}'