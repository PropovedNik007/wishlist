from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    """ Таблица "Товар"

    id
    Название товара

    """
    title = models.CharField(max_length=120, verbose_name='Название')
    link = models.URLField(verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """
    id
    name
    owner
    products
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
