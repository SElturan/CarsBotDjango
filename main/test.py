from django.db import models
from faker import Faker
from .models import TelegramUser

def func():
    fake = Faker()

    # Генерация 10 тыс. записей
    for _ in range(10000):
        # Создание случайных данных с помощью Faker
        user_id = fake.random_number(digits=10)
        role = fake.random_element(['user', 'driver', 'admin', 'UK'])
        first_name = fake.first_name()
        phone_number = fake.phone_number()

        # Создание экземпляра модели и сохранение его в базе данных
        user = TelegramUser(user_id=user_id, role=role, first_name=first_name, phone_number=phone_number)
        user.save()
