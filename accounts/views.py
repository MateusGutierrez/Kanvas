from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Account
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import AccountSerializer


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
