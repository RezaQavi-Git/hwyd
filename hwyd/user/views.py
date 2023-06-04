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
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email =request.POST.get('email') 
        password =request.POST.get('password')

        print(email, password)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return redirect('/')
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
                return redirect('login')
        
        except Exception as e:
            error_message = str(e)

        return render(request, 'signup.html', {'error_message': error_message})
    
    return render(request, 'signup.html')


def rate(request):
    if request.method == 'POST':
        email = request.POST['email']
        rate = int(request.POST['rate'])
        
        try:
            # Retrieve the user based on the provided email
            user = User.objects.get(email=email)
            
            print(user)
            # Create a FeelRate object and associate it with the user
            feel_rate = FeelRate(rate=rate, time=datetime.now(), reporter=user)
            feel_rate.save()

            user.list_of_feelings.add(feel_rate.id)            
            # Perform additional actions if needed
            
            return redirect('/')  # Replace 'home' with the appropriate URL name
        
        except User.DoesNotExist:
            error_message = 'User with the provided email does not exist'
        except Exception as e:
            error_message = str(e)
        
        # Render the rating page with the error message
        return render(request, 'rate.html', {'error_message': error_message})
    
    return render(request, 'rate.html')
def logout(request):
    logout(request)
    return redirect('login')


def users(request):
    members = User.objects.all().values()
    print(members)
    template = loader.get_template('home.html')
    context = {
        'users': members[0]
    }
    return HttpResponse(template.render(context, request))


# def rating(request):
#     if request.method == 'POST':
#         rate =request.POST.get('rating') 
#         print(rate, type(rate))
#         template = loader.get_template('rated.html')
#         return HttpResponse(template.render())
