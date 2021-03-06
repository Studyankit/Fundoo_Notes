import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserProfile


# Create your views here.

def user_registration(request):
    try:
        if request.method == "POST":
            register = json.loads(request.body)
            print(register)
            u = UserProfile.objects.create(user_name=register.get('user_name'))
            print(u)
            u.save()
            # Check username is present or not
            # user_check = UserProfile.objects.filter(user_name=register.get("user_name"))
            # if request.body == user_check:
            #     return JsonResponse({
            #         'message': 'User already exists'
            #     })
            # else:
            #     user_login(request)
            # print("welcome", user_check)
            return JsonResponse({
                'message': 'User added successfully'
            })
    except Exception as e:
        print(e)
        return JsonResponse({
            'message': 'User not there or enter proper registration details'
        })


def user_login(request):
    try:
        if request.method == "GET":
            login = json.loads(request.body)
            user_check_login = UserProfile.objects.get(user_name=login.get("user_name"), email=login.get("email"))
            print(user_check_login)
            return JsonResponse({
                'message': 'User already exists'
            })
    except Exception as e:
        return JsonResponse({
            'message': 'user needs to be added'
        })


