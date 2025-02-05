from django.contrib import admin
from foodaskerapp.models import Restaurant,MenuItem,OrderDetails,Delivery


# Register your models here.
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(OrderDetails)
admin.site.register(Delivery)
