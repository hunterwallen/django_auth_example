from rest_framework import serializers
from .models import UserAccount
from django.contrib.auth.hashers import make_password, check_password

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password')
    def create(self, validated_data):
        user = UserAccount.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        # user.password(validated_data['password'])
        user.save()
        return user
    def update(self, instance, request):
        user = UserAccount.objects.get(email=request['email'])
        user.update(password=make_password(request['password']))
        # user.password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password')
    def update(self, instance, request):
        #grab user object with matching email
        user = UserAccount.objects.get(email=request['email'])
            #compare passwords
        if check_password(request["password"], user["password"]):
            return {'id': user['id'], 'username': user['username']}
        else:
            return {}
