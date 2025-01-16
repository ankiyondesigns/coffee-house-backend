from django.db import models

class CoffeeProduct(models.Model):
    image = models.ImageField(upload_to='coffee_products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    measurement_grams = models.PositiveIntegerField()

    def __str__(self):
        return self.name if self.name else 'Unnamed Coffee Product'

