from django.contrib import admin

from .models import User, FeelRate
# Register your models here.
class UserAdmin(admin.ModelAdmin):
      list_display = ("email", "nickname")

class FeelRateAdmin(admin.ModelAdmin):
      list_display = ("reporter", "rate", "time")

admin.site.register(User, UserAdmin)
admin.site.register(FeelRate, FeelRateAdmin)

