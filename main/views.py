from django.shortcuts import render

from main.models import News, Address


def home(requests):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(requests, 'main/index.html', context)

def address(requests):
    address = Address.objects.all()
    context = {
        'address': address
    }
    return render(requests, 'main/address.html', context)
