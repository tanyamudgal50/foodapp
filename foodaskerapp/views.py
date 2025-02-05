from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from foodaskerapp.forms import UserForm, RestaurantForm,MenuItemForm,OrderDetailsForm,DeliveryForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User


def home(req):
    return redirect(restaurant_home)

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(req):
    return render(req,'restaurant/home.html',{})

def restaurant_sign_up(req):
    user_form = UserForm() 
    restaurant_form = RestaurantForm()

    if req.method == "POST":
        user_form = UserForm(req.POST)
        restaurant_form = RestaurantForm(req.POST, req.FILES)

        if user_form.is_valid() and restaurant_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit= False)
            new_restaurant.user = new_user
            new_restaurant.save
            

            login(req,authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect (restaurant_home)

    return render(req,'restaurant/sign_up.html',{
        "user_form" : user_form,
        "restaurant_form" :  restaurant_form
    })

def restaurant_add_menu_item(req):  
       Menu = Menu.objects.all
       return render(req,'restaurant/Menu-Item.html',{})

def restaurant_Order_Details(req):
    OrderDetails = OrderDetails.objects.filter(customer_email=req.user.email, status='Pending').first()
    return render(req,'restaurant/Order-Details.html',{})

def restaurant_delivery(req):
    Delivery = Delivery.objects.all()
    if req.method == 'POST':
        form = DeliveryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-delivery')  # Redirect to refresh the page
    else:
        form = DeliveryForm()

    return render(req, 'restaurant_delivery.html', {'form': form, 'deliveries': Delivery})

  