"""Products app models"""

from django.db import models


class Product(models.Model):
    """My ecommerce product model"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    RATING_CHOICES = (
        (1, 'Muy malo'),
        (2, 'Malo'),
        (3, 'Regular'),
        (4, 'Bueno'),
        (5, 'Muy bueno'),
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        """Returns a product string representation"""
        return '{name} - ${price}'.format(name=self.name, price=self.price)
