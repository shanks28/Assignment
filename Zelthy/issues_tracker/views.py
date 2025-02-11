from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Ticket
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import json
# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("Hello man")
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            email = data.get("email")

            if not username or not password or not email:
                return JsonResponse({"message": "Missing field", "status_code": 400}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": "Username already taken", "status_code": 400}, status=400)

            user_obj = User.objects.create_user(username=username, password=password, email=email)

            return JsonResponse({"message": "User registered successfully", "username": user_obj.username, "email": user_obj.email}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format", "status_code": 400}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e), "status_code": 500}, status=500)

    return JsonResponse({"message": "Invalid request method", "status_code": 405}, status=405)
@csrf_exempt
def login_user(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            username=data.get("username")
            password=data.get("password")
            if not username or not password:
                return JsonResponse({"Message":"Missing field","status_code":400})
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return JsonResponse({"Message":"User logged in","status_code":200})
            return JsonResponse({"Message":"Wrong username or password","status_code":400})
        except Exception as e:
            return JsonResponse({"Message":str(e)})
@csrf_exempt
@login_required(login_url="/login/")
def create_ticket(request):
    if request.method=="POST":
        data=json.loads(request.body)
        assignee_username=data.get("assignee_username")
        assignee_user=None
        if assignee_username:
            try:
                assignee_user=User.objects.get(username=assignee_username)
            except Exception as e:
                return JsonResponse({"Message":"User not found","status_code":400})
        ticket=Ticket.objects.create(
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status"),
            assignee=assignee_user
        )
        return JsonResponse({"Message":"Ticket created","status_code":200})
@csrf_exempt
@login_required(login_url="/login/")
def update_ticket(request):
    if request.method=="PUT":
        try:
            data=json.loads(request.body)
            issue=Ticket.objects.get(title=data.get("title"))
            issue.description=data.get("description")
            issue.status=data.get("status")
            assignee=data.get("assignee")
            if assignee:
                try:
                    issue.assignee=User.objects.get(username=assignee)
                except Exception as e:
                    return JsonResponse({"Message":"User not found","status_code":400})
            issue.save()
            return JsonResponse({"Message":"Ticket updated","status_code":200})
        except Exception as e:
            return JsonResponse({"Message":str(e)})
@csrf_exempt
def logout_user(request):
    if request.method=="POST":
        logout(request)
        return JsonResponse({"Message":"User logged out","status_code":200})
    return JsonResponse({"message":"Invalid request method","status_code":405})