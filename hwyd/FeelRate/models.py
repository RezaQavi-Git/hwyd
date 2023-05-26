from django.db import models

from ..members.models import Member
# Create your models here.
class FeelRate(models.Model):
  member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
  date = models.DateField()
  rate = models.IntegerField()
  