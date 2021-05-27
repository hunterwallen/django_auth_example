from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAccountSerializer
from .models import UserAccount
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json



class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserAccountSerializer # tell django what serializer to use



class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer


def check_login(request):
    if request.method=='GET':
        return JsonResponse({})
        #grab user object with matching email
    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        email = jsonRequest['email']
        password = jsonRequest['password']
        if UserAccount.objects.get(email=email):
                        #compare passwords
            user = UserAccount.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'email': user.email})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})
