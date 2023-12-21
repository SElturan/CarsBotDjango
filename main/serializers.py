from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.user_id')


    class Meta:
        model = Address
        fields = ('id','user_id', 'city', 'house_number', 'address', )

    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = TelegramUser.objects.get(user_id=user_id)
        address = Address.objects.create(user=user, **validated_data)
        return address

class NumberCarSerializers(serializers.ModelSerializer):

    user_id = serializers.IntegerField(source='user.user_id')


    class Meta:
        model = NumberCar
        fields = ('id','user_id', 'car_num', 'default_num', 'vin', 'car_brand', 'car_model', 'car_year', 'power','created_at', 'updated_at', )

    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = TelegramUser.objects.get(user_id=user_id)
        numbercar = NumberCar.objects.create(user=user, **validated_data)
        
        return numbercar
    
class AddressDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('city', 'house_number', 'address', )



class AddressUKSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.user_id')
    address = AddressDetailSerializer(many= True)


    class Meta:
        model = AddressUK
        fields = ('id','user_id', 'nick', 'address',)

    def create(self, validated_data):
        user_id = validated_data.pop('user').get('user_id')
        user = TelegramUser.objects.get(user_id=user_id)
        address = AddressUK.objects.create(user=user, **validated_data)
        return address


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('id', 'user_id', 'role','first_name', 'phone_number','ban' )


class TemplateUkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateUk
        fields = ('id', 'template_id', 'template', )