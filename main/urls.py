from django.urls import path

from main.views import home, address

app_name = 'main'
urlpatterns = [
    path('', home, name='home'),
    path('address/', address, name = 'address' )
]