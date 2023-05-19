# Подключаем статус
import requests
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from django.shortcuts import render

from rest_framework import status
# Подключаем компонент для ответа
from rest_framework.response import Response
# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView
# Подключаем компонент для прав доступа

from rest_framework.views import APIView

# Подключаем модель User
from .models import User, AuthtokenToken
# Подключаем UserRegistrSerializer
from .serializers import UserRegistrSerializer
from .telega_auth import HashCheck
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_protect


# Создаём класс RegistrUserView

class RegistrUserView(CreateAPIView):
    # Добавляем в queryset
    queryset = User.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = UserRegistrSerializer
    # Добавляем права доступа
    permission_classes = [AllowAny]


    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        # Добавляем UserRegistrSerializer
        serializer = UserRegistrSerializer(data=request.data)
        # Создаём список data
        data = {}
        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохраняем нового пользователя
            serializer.save()
            # Добавляем в список значение ответа True
            data['response'] = True
            # Возвращаем что всё в порядке
            return Response(data, status=status.HTTP_200_OK)
        else:  # Иначе
            # Присваиваем data ошибку
            data = serializer.errors
            # Возвращаем ошибку
            return Response(data)

#def telega(request):
    #return render(request, "telega.html")


def base(request):
    return render(request, "base.html")


class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        client_token = AuthtokenToken.objects.filter(user=request.user)
        HttpResponse().set_cookie('Authorization', client_token[0].key, max_age=None)
        return HttpResponse(f"Logged in {user} {client_token[0].key}")


def get_tok(request):
    client_token = AuthtokenToken.objects.filter(user=request.user)[0].key
    html = HttpResponse(client_token)
    html.set_cookie('Token', client_token, max_age = None)

    return html

def delete_co(request):
    if request.COOKIES.get('WWW-Authenticate'):
       response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
       response.delete_cookie("WWW-Authenticate")
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response