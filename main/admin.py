from django.contrib import admin
from django.contrib.admin import display
from .models import TelegramUser, Address, AddressUK, NumberCar, TemplateUk

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'role', 'first_name','ban', 'phone_number',  'created_at', 'updated_at')
    list_display_links = ('id', 'user_id', 'role',)
    list_filter = ('role','created_at', 'updated_at')
    search_fields = ('user_id', 'first_name', 'phone_number', )
    list_editable = ['ban']
    


@admin.register(NumberCar)
class NumberCarAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'car_num','default_num','vin',  'car_brand', 'car_model', 'car_year', 'power','created_at', 'updated_at')
    list_display_links = ('id', 'user')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__first_name',  'car_num','vin', 'car_brand', 'car_model', 'car_year', 'power')
    autocomplete_fields = ('user',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'city', 'address', 'house_number',  'created_at', 'updated_at', )
    list_display_links = ('id', 'user')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user', 'address',)
    autocomplete_fields = ('user',)


@admin.register(AddressUK)
class AddressUKAdmin(admin.ModelAdmin):
    filter_horizontal = ('address', )
    list_display = ('id','user', 'address_list','nick', 'created_at', 'updated_at')
    list_display_links = ('id', 'user')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__first_name', 'user__phone_number', 'nick')
    autocomplete_fields = ('user',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        try:
            # Пытаемся найти пользователя по номеру телефона
            user = TelegramUser.objects.get(phone_number=search_term)
            queryset |= self.model.objects.filter(user=user)
        except TelegramUser.DoesNotExist:
            pass

        return queryset, use_distinct


    @display(description='Адреса')
    def address_list(self, obj):
        return ", ".join([a.address for a in obj.address.all()])
    
@admin.register(TemplateUk)
class TemplateUkAdmin(admin.ModelAdmin):
    list_display = ('id', 'template_id', 'template')


