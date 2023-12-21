from .models import TelegramUser, Address, AddressUK, NumberCar, TemplateUk
from .serializers import TelegramUserSerializer, AddressSerializer, AddressUKSerializer, NumberCarSerializers, TemplateUkSerializer
from rest_framework import viewsets
import django_filters.rest_framework


class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user_id', 'role')


    


class NumberCarViewSet(viewsets.ModelViewSet):
    queryset = NumberCar.objects.all()
    serializer_class = NumberCarSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user__user_id', 'car_num', 'default_num')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user__user_id', 'address', 'house_number')
    search_fields = ('user__user_id', 'address', 'house_number')



class AddressUKViewSet(viewsets.ModelViewSet):
    queryset = AddressUK.objects.all()
    serializer_class = AddressUKSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user__user_id', 'address__address', 'address__house_number',)



class TemplateUkViewSet(viewsets.ModelViewSet):
    queryset = TemplateUk.objects.all()
    serializer_class = TemplateUkSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('template_id', )






