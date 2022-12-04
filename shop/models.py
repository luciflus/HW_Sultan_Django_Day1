from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование товара')
    price = models.IntegerField(default=0)

class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО клиента')
    age = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="purchases")
    date_purchase = models.DateField(auto_now_add=True, verbose_name='Дата покупки')
