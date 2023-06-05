from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import User, FeelRate
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from datetime import datetime

def handler_404(request, exception):
    return render(request, '404.html')

def home(request):
    nickname = request.COOKIES.get('nickname')
    if nickname:
        context = {'nickname': nickname}
        return render(request, 'home.html', context)
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        email =request.POST.get('email') 
        password =request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                response = redirect('home')
                response.set_cookie('nickname', user.get_nickname())
                return response
            else:
                error_message = 'Invalid password'
        except User.DoesNotExist:
            error_message = 'Invalid username' 

        return render(request, 'login.html', {'error_message': error_message})
    
        
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        nickname = request.POST['nickname']
        password = request.POST['password']

        try:
            user_exists = User.objects.filter(email=email).exists()
            
            if user_exists:
                error_message = 'Email is already taken'
            else:
                user = User(email=email, nickname=nickname, password=password)
                user.save()
                response = redirect('home')
                response.set_cookie('nickname', nickname)
                return response
        
        except Exception as e:
            error_message = str(e)

        return render(request, 'signup.html', {'error_message': error_message})
    
    return render(request, 'signup.html')


def rating(request):
    if request.method == 'POST':
        email = request.POST['email']
        rate = int(request.POST['rate'])
        
        try:
            user = User.objects.get(email=email)
            
            print(user)
            feel_rate = FeelRate(rate=rate, time=datetime.now(), reporter=user)
            feel_rate.save()
            user.list_of_feelings.add(feel_rate.id)            
            return redirect('home')
        
        except User.DoesNotExist:
            error_message = 'User with the provided email does not exist'
        except Exception as e:
            error_message = str(e)
        
        return render(request, 'rating.html', {'error_message': error_message})
    
    return render(request, 'rating.html')

def users(request):
    members = User.objects.all().values()
    print(members)
    template = loader.get_template('home.html')
    context = {
        'users': members[0]
    }
    return HttpResponse(template.render(context, request))


def test(request):

    return render(request, 'test.html')