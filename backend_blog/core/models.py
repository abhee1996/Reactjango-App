from django.db import models
from django.conf import settings

# Create your models here.

class Items(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrderItems(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItems)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BinaryField(default=False)

    def __str__(self):
        return self.user.username


