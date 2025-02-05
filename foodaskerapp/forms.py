from django import forms
from django.contrib.auth.models import User
from foodaskerapp.models import MenuItem, Restaurant,OrderDetails,Delivery

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required= True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name','last_name','email']

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','phone','address','logo']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['Name', 'description', 'price']

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['customername', 'customeremail','status']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['address', 'delivery_status','delivery_date']

