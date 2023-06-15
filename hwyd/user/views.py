from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import User, FeelRate
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
import json
import random



def handler_404(request, exception):
    return render(request, "404.html")


def home(request):
    email = request.COOKIES.get("email")
    if email:
        context = {"nickname": User.objects.get(email=email).get_nickname().upper()}
        return render(request, "home.html", context)
    else:
        return redirect("login")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                response = redirect("home")
                response.set_cookie("email", user.get_email())
                return response
            else:
                error_message = "Invalid password"
        except User.DoesNotExist:
            error_message = "Invalid username"

        return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


def logout(request):
    response = redirect("login")
    response.delete_cookie('email')

    return response


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        nickname = request.POST["nickname"]
        password = request.POST["password"]

        try:
            user_exists = User.objects.filter(email=email).exists()

            if user_exists:
                error_message = "Email is already taken"
            else:
                user = User(email=email, nickname=nickname, password=password)
                user.save()
                response = redirect("home")
                response.set_cookie("email", email)
                return response

        except Exception as e:
            error_message = str(e)

        return render(request, "signup.html", {"error_message": error_message})

    return render(request, "signup.html")


def rate(request):
    if request.method == "POST":     
        email = request.COOKIES.get("email")
        rate = int(request.POST["rate"])
        try:
            user = User.objects.get(email=email)

            feel_rate = FeelRate(rate=rate, time=datetime.now(), reporter=user)
            feel_rate.save()
            user.list_of_feelings.add(feel_rate.id)
            return render(request, 'rated.html')

        except User.DoesNotExist:
            error_message = "User with the provided email does not exist"
        except Exception as e:
            error_message = str(e)

        return render(request, "rating.html", {"error_message": error_message})

    return redirect('home')


def history(request):
    email = request.COOKIES.get("email")
    user = User.objects.get(email=email)

    now = datetime.now()
    past = now - timedelta(days=7)
    rates = user.get_rates(past, now)    
    x_data = [rate.get_time() for rate in rates]
    y_data = [rate.get_rate() for rate in rates]
    chart_data = {
        "labels": x_data,
        "datasets": [
            {
                "label": "Rates",
                "data": y_data,
                "borderColor": "#50bef6",
                "fill": False,
            }
        ],
    }
    chart_data_json = json.dumps(chart_data)
    return render(request, "history.html", {"chart_data_json": chart_data_json})


def test(request):


    x_data = ["January", "February", "March", "April", "May", "June"]
    y_data = [10, 20, 15, 25, 18, 30]

    chart_data = {
        "labels": x_data,
        "datasets": [
            {
                "label": "history",
                "data": y_data,
                "borderColor": "green",
                "fill": False,
            }
        ],
    }

    chart_data_json = json.dumps(chart_data)
    return render(request, "test.html", {"chart_data_json": chart_data_json})
