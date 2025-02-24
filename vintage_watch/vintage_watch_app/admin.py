from django.contrib import admin
from .models import Product
from .models import seller_data
from .models import sign_up

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price','shipping_charge','watch_type', 'payment_method', 'return_policy')
    list_filter = ('watch_type', 'payment_method', 'return_policy')
@admin.register(seller_data)
class seller_Details(admin.ModelAdmin):
    list_display = ('id','name','description', 'price','shipping_charge','watch_type', 'payment_type', 'return_policy', 'delivery_time')
    def image_display(self, obj):
        return obj.image.url if obj.image else "No Image"
@admin.register(sign_up)
class sign_up_d(admin.ModelAdmin):
    list_display = ('name', 'user_name', 'email_add', 'password')
