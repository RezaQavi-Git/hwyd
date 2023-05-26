from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import User


def users(request):
    members = User.objects.all().values()
    print(members)
    template = loader.get_template('home.html')
    context = {
        'users': members[0]
    }
    return HttpResponse(template.render(context, request))


def rating(request):
    if request.method == 'POST':
        rate =request.POST.get('rating') 
        print(rate, type(rate))
        template = loader.get_template('rated.html')
        return HttpResponse(template.render())
