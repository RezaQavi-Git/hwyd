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
  
  def get_email(self):
     return self.email
  
  def get_rates(self, start, end):
     rates, days = [], []
     for rate in self.list_of_feelings.all():
        if rate.get_time() not in days:
         if rate.get_time() >= start.strftime("%Y-%m-%d") and rate.get_time() <= end.strftime("%Y-%m-%d"):
            rates.append(rate)
            days.append(rate.get_time())
     return rates

  def check_password(self, password):
     return self.get_password() == password

class FeelRate(models.Model):
   rate = models.IntegerField()
   time = models.DateTimeField()
   reporter = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)


   def get_rate(self):
      return self.rate

   def get_time(self):
      return self.time.strftime("%Y-%m-%d")

   def __str__(self):
      return f'Rate: {self.rate}'