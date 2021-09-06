from django.db import models


# Create your models here.
class Product(models.Model):
    """ Таблица "Товар"

    id
    Название товара

    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
