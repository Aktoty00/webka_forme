from django.db import models
from django.contrib.auth.models import User

class UserProductManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(user=user)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.name, self.price)


class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_products')
    count = models.IntegerField(default=0)

    objects = UserProductManager()

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.id, self.user, self.product, self.count)
