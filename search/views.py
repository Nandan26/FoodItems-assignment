from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, FoodDish, Cuisine
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    """
    This function is responsible for rendering home page with passing context dictionary to template

    takes http request as argument

    """

    # get search query from http request
    query = request.GET.get('q') if request.GET.get('q') != None else ''

    # food_items based on search query 
    food_items = FoodDish.objects.filter(
        Q(name__icontains = query)
    ).order_by(
        '-restaurant__average_rating',
        '-restaurant__total_reviews').values('name','price','restaurant_id','restaurant__name','restaurant__average_rating')

    # paginate the results
    paginator = Paginator(food_items, 100)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    
    context = {
        'food_items': page_obj,
        'query': query,
    }
    
    return render(request, 'home.html', context)

def restaurant_view(request,id):
    """
    This function is responsible for rendering restaurant page with passing context dictionary to template

    takes http request as first argument
    takes restaurant id as second argument

    """

    # get the restaurant based on the id
    restaurant = Restaurant.objects.get(id = id)

    # find all the dishes served by the restaurant
    dishes = FoodDish.objects.filter(restaurant_id = id)

    #cuisines available in the restaurant
    cuisines = Cuisine.objects.filter(restaurant = restaurant)
    context = {
        'restaurant' : restaurant,
        'food_items' : dishes,
        'cuisines': cuisines
    }

    return render(request, 'restaurant.html', context)