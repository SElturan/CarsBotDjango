from django.db import models
from django.core.exceptions import ValidationError



class TelegramUser(models.Model):

    ROLE_CHOICES = (
        ('user','Пользователь'),
        ('driver', 'Водитель'),
        ('admin', 'Администратор'),
        ('UK', 'УК'),

    )

    user_id = models.BigIntegerField(unique=True, verbose_name='ID телеграм')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name='Роль')
    first_name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    phone_number = models.CharField(max_length=100, blank=True, verbose_name='Номер телефона')
    ban = models.BooleanField(default=False, verbose_name='Бан пользователя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата входа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')




    def __str__(self):
        return f'{self.first_name}'
    
    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'


class NumberCar(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    car_num = models.CharField(max_length=50, null=True, blank=True, verbose_name='Номер авто')
    default_num = models.BooleanField(default=False, verbose_name='Номер по умолчанию')
    vin = models.CharField(max_length=200, null=True, blank=True, verbose_name='VIN')
    car_brand = models.CharField(max_length=100, null=True, blank=True, verbose_name='Марка авто')
    car_model = models.CharField(max_length=100, null=True, blank=True, verbose_name='Модель авто')
    car_year = models.BigIntegerField( null=True, blank=True, verbose_name='Год авто')
    power = models.CharField(max_length=100, null=True, blank=True, verbose_name='Мощность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only run validation on creation
            num_cars = NumberCar.objects.filter(user=self.user).count()
            if num_cars >= 3:
                raise ValidationError('The user already has the maximum number of cars.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}-{self.car_num}'
    
    class Meta:
        verbose_name = 'Авто пользователя'
        verbose_name_plural = 'Авто пользователей'
        unique_together = ('user', 'car_num')



class Address(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    house_number = models.CharField(max_length=100, blank=True, verbose_name='Номер дома')
    address = models.CharField(max_length=100, blank=True, verbose_name='Улица')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')



    def __str__(self):
        return f'{self.city}-{self.address}-№{self.house_number}'
    
    class Meta:
        verbose_name = 'Адрес пользователя'
        verbose_name_plural = 'Адреса пользователей'
        unique_together = ('user', 'address')




class AddressUK(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    nick = models.CharField(max_length=20,null=True,blank=True,verbose_name='Псевдоним')
    address = models.ManyToManyField(Address, related_name='address_uk', verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')



    def __str__(self):
        return f'{self.address}'
    

    
    class Meta:
        verbose_name = 'УК'
        verbose_name_plural = 'УК'
        


class TemplateUk(models.Model):
    template_id = models.CharField(max_length=20, null=True, blank=True, verbose_name='краткое наименование шаблона')
    template = models.TextField(verbose_name='Текст для рассылки')

    def __str__(self):
        return self.template_id

    class Meta:
        verbose_name = 'Шаблон УК'
        verbose_name_plural = 'Шаблоны УК'

