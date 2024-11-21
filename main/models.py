from django.db import models

class News(models.Model):
    title = models.CharField('Имя',max_length=50)
    description = models.TextField('Описание',max_length=1000)
    image = models.ImageField(upload_to='news-img')
    date = models.DateTimeField(auto_now_add=True)
    aftor = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Address(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title