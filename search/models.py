from django.db import models


class Restaurant(models.Model):
    """
        Restaurant details table
    
    """

    name = models.CharField(max_length = 100)

    area = models.CharField(max_length = 250)

    total_reviews = models.IntegerField(blank = True, null=True)

    average_rating = models.DecimalField(max_digits = 2, decimal_places = 1, blank = True, null=True)

    lot_long = models.CharField(max_length = 50)

    average_cost_for_2 = models.DecimalField(max_digits = 7, decimal_places = 2, blank=True, null=True)

    online_delivery = models.BooleanField(default=False)

    table_booking = models.BooleanField(default=False)
    
    delivering_now = models.BooleanField(default=False)

    table_reservation_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FoodDish(models.Model):
    """
        Dishes information for individual restuarant
    
    """
    name = models.CharField(max_length = 100)

    price = models.DecimalField(max_digits = 7, decimal_places = 2)

    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    """
        Cuisine table
    
    """

    name = models.CharField(max_length = 100)

    restaurant = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.name




