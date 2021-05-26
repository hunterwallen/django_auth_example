from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAccountSerializer, UserLoginSerializer
from .models import UserAccount



class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserAccountSerializer # tell django what serializer to use



class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer


class UserAccountLogin(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserLoginSerializer # tell django what serializer to use

class UserAccountLoginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer
