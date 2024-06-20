from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dishes/')
    description = models.TextField()
    spicy_level = models.IntegerField(default=0)
    is_nutty = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
