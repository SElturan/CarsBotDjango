from django.urls import path

from .views import TelegramUserViewSet, AddressViewSet, AddressUKViewSet, NumberCarViewSet, TemplateUkViewSet

app_name = "main"

urlpatterns = [
    path('user/', TelegramUserViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('user/<int:pk>/', TelegramUserViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    path('address/', AddressViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('address/<int:pk>/', AddressViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

    path('address_uk/', AddressUKViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('address_uk/<int:pk>/', AddressUKViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

    path('number_car/', NumberCarViewSet.as_view(
        
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('number_car/<int:pk>/', NumberCarViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

    
    path('template/', TemplateUkViewSet.as_view(
        
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('template/<int:pk>/', TemplateUkViewSet.as_view(
        {
            'get':'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),

]