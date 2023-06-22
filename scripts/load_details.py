import csv
import json
import decimal
from search.models import Restaurant, FoodDish, Cuisine

def run():
    """
        This function reads data from csv file and saves it to the sqlite3 database using django ORM
     
    """

    # delete all the objects from database
    Restaurant.objects.all().delete()
    FoodDish.objects.all().delete()
    Cuisine.objects.all().delete()


    #read the csv file
    with open('restaurants_small.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        i = 1

        #read each row
        for row in reader:
            print(f"Record no. {i} is being executed")
            i = i+1

            # get the restaurant information from the CSV file
            restaurant_name = row[1]

            restaurant_location = row[2]

            lat_long = row[4]

            # check if more information is available
            if len(row[5]) > 0:
                info = json.loads(row[5])

                total_votes = int(info["user_rating"]["votes"])

                rating = decimal.Decimal(info["user_rating"]["aggregate_rating"])

                average_cost_for_2 = decimal.Decimal(info["average_cost_for_two"])

                online_delivery = bool(info["has_online_delivery"])

                table_booking = bool(info["has_table_booking"])
    
                delivering_now = bool(info["is_delivering_now"])

                table_reservation_supported = bool(info["is_table_reservation_supported"])

                restaurant = Restaurant.objects.create(
                    name = restaurant_name, 
                    area = restaurant_location, 
                    lot_long = lat_long, 
                    average_rating = rating, 
                    total_reviews = total_votes, 
                    average_cost_for_2 = average_cost_for_2, 
                    online_delivery = online_delivery, 
                    table_booking = table_booking,
                    delivering_now = delivering_now,
                    table_reservation_supported = table_reservation_supported
                )

                for cuisine in info["cuisines"].split(","):
                    name = cuisine

                    cuisine, _ = Cuisine.objects.get_or_create(name = name)

                    cuisine.restaurant.add(restaurant)
           
            else:
                restaurant = Restaurant.objects.create(name = restaurant_name, area = restaurant_location, lot_long = lat_long)
            
            # read the menu items
            menu_items = json.loads(row[3])

            # iterate over the menu items and create food dish record for each of them
            for key,value in menu_items.items():
                dish_name = key
                value = value.split()
                dish_price = decimal.Decimal(value[0])

                FoodDish.objects.create(name = dish_name, price = dish_price, restaurant = restaurant)

