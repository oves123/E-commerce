from django.contrib import admin
from django.urls import path
from vintage_watch_app import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.custom_404_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up_f, name='sign'),
    path('selling/', views.selling_page, name='selling'),
    path('mens_watch/', views.mens_watchs, name='men_watch'),
    path('womens_watch/', views.women_watchs, name='women_watch'),
    path('add_product/', views.add_product, name='add_pro'),
    path('product_details/<int:product_id>', views.product_detail, name='pro_d'),
    path('contact/', views.contact, name='contact'),
    path('forgot_password/', views.forgot_password, name='forgot'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

