from django.core.validators import RegexValidator
from django.db import models  # Подключаем работу с моделями
# Подключаем классы для создания пользователей

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Создаем класс менеджера пользователей
class MyUserManager(BaseUserManager):
    # Создаём метод для создания пользователя
    def _create_user(self, email, password, **extra_fields):
        # Проверяем есть ли Email
        if not email:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Email")
        # Проверяем есть ли логин

        # Делаем пользователя
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем всё остальное
        user.save(using=self._db)
        # Возвращаем пользователя
        return user

    # Делаем метод для создание обычного пользователя
    def create_user(self, email, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, password)



# Создаём класс User
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)  # Идентификатор
    email = models.EmailField(max_length=100, unique=True, blank=False)  # Email
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, default="", blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True, blank=False)
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа

    USERNAME_FIELD = 'email'  # Идентификатор для обращения


    objects = MyUserManager()  # Добавляем методы класса MyUserManager

    # Метод для отображения в админ панели
    def __str__(self):
        return self.email