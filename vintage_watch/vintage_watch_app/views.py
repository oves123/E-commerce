from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Product
from .models import seller_data
from .models import sign_up
from django.contrib import messages # type: ignore # type: ignore

# Create your views here.
def index(request):
    data = ''
    seller_details = ''
    query = request.GET.get('search')
    query = query.strip() if query else ''
    username = request.session.get("username", "Guest")
    products_s = Product.objects.none()  # Get the search term from the HTML form
    if query:
        products_s = seller_data.objects.filter(name__icontains=query)
    else:
        data = Product.objects.all()
        seller_details = seller_data.objects.all()
    return render(request, 'index.html', {'data':data, 'seller_details':seller_details,'query': query, 'products_s':products_s, "username": username})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session["username"] = request.POST.get("username")
        data = sign_up.objects.all()
        for data in data:
            if username == data.user_name and password == data.password: 
                return redirect('index')
            else:
                messages.error(request, 'Incorrect email or password.') 
    return render(request, 'login.html')
def sign_up_f(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        username = request.POST.get('username')
        email_add = request.POST.get('emailadd')
        password = request.POST.get('password')
        sign_up.objects.create(name=name,user_name=username,email_add=email_add,password=password)
        messages.success(request, "registration successful!")
        return redirect('login')
    return render(request, 'sign_up.html')
def selling_page(request):
    if request.method == "POST":
        name = request.POST.get("watch_name")
        description = request.POST.get("watch_description")
        watch_type = request.POST.get("watch_type")
        price = request.POST.get("watch_price")
        shipping_charge = request.POST.get("shipping_charge")
        return_policy = request.POST.get("return_policy")
        delivery_time = request.POST.get("delivery_time")
        payment_type = request.POST.get("payment_type")
        uploaded_image = request.POST.get('image')
        # Save to database
        seller_data.objects.create(
            name=name,
            description=description,
            price=price,
            watch_type=watch_type,
            shipping_charge=shipping_charge,
            delivery_time=delivery_time,
            image=uploaded_image,
            payment_type=payment_type,
            return_policy=return_policy,
        )
        print("data added")
        messages.success(request, "product saved successfully!")
        return redirect('index')
    return render(request, 'selling.html')
def women_watchs(request):
    womens_watch_details = seller_data.objects.filter(watch_type='Women')
    return render(request, 'women_watch.html',{'mens_watch':womens_watch_details})
def add_product(request):
    return render(request, 'addproduct.html')
def mens_watchs(request):
    mens_watch_details = seller_data.objects.filter(watch_type='Men')
    return render(request, 'men_watch.html', {'mens_watch':mens_watch_details})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # product1 = get_object_or_404(seller_data, id=seller_data.id)
    return render(request, 'product_details.html',{'product': product})


def contact(request):
    return render(request, 'contact.html')
def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        # Check if passwords match
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("forgot")
        try:
            user = sign_up.objects.get(user_name=username)
            user.password = new_password
            user.save()
            messages.success(request, "Password updated successfully!")
            return redirect("login")  # Redirect after update
        except sign_up.DoesNotExist:
            messages.error(request, "User not found.")
        return redirect("forgot")
    return render(request, 'forgot_pass.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)