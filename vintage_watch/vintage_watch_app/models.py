from django.db import models
# save selling watch data
class seller_data(models.Model):
    Men = 'Men'
    Women = 'Women'
    WATCH_TYPE_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
    ]
    Credit_Card = 'Credit Card'
    PayPal = 'PayPal'
    Gpay = 'Gpay'
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Gpay', 'Gpay'),
    ]
    Yes = 'Yes'
    No = 'No'
    RETURN_POLICY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    watch_type = models.CharField(max_length=50, choices=WATCH_TYPE_CHOICES, default=Men)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2)
    return_policy = models.CharField(max_length=50, choices=RETURN_POLICY_CHOICES, default=Yes)
    delivery_time = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default=Credit_Card)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    Men = 'men'
    Women = 'women'
    WATCH_TYPE_CHOICES = [
        ('men', 'men'),
        ('women', 'women'),
    ]
    Credit_Card = 'Credit Card'
    PayPal = 'PayPal'
    Gpay = 'Gpay'
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Gpay', 'Gpay'),
    ]
    Yes = 'Yes'
    No = 'No'
    RETURN_POLICY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='img/')  # Product Image
    name = models.CharField(max_length=255)  # Watch Name
    description = models.TextField()  # Watch Description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Watch Price
    delivery_time = models.CharField(max_length=50)  # Delivery Time
    return_policy = models.CharField(max_length=3, choices=RETURN_POLICY_CHOICES, default=Yes)  # Accepts only 'Yes' or 'No'
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default=Credit_Card)  # Only Credit Card or PayPal
    watch_type = models.CharField(max_length=10, choices=WATCH_TYPE_CHOICES, default=Men)  # Only Men or Women
    shipping_charge = models.DecimalField(max_digits=6, decimal_places=2)  # Shipping Charge

    
    def __str__(self):
        return self.name  # Display name in Django Admin\
    


class sign_up(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email_add = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
