from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'), 
    path('logout/', views.logout_user, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('admin/', views.admin,name='admin'),
    path('appartment/', views.appartment,name='appartment'),
    path('adminappart/', views.adminappart,name='adminappart'),
    path('register/', views.register_type, name='register_type'),
    path('register/normal_user/', views.register_normal_user, name='register_normal_user'),
    path('register/hotel_owner/', views.register_hotel_owner, name='register_hotel'),
    path('normal_user_home/', views.normal_user_home, name='normal_user_home'),
    path('hotel_owner_home/', views.hotel_owner_home, name='hotel_owner_home'),
    path('cab_driver_home/', views.cab_driver_home, name='cab_driver_home'),
    path('appartments/', views.appartments, name='appartments'),
    path('appartment_user_view/', views.appartment_user_view, name='appartment_user_view'),
    path('all_users/', views.all_users, name='all_users'),
    path('booking/<str:name>', views.booking, name='booking'),
    path('bookings/<str:name>', views.bookings, name='bookings'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('editbtn/<int:id>/', views.editbtn, name='editbtn'),
    path('payment/<str:name>', views.payment, name='payment'),
    path('pay/<str:name>', views.pay, name='pay'),
    path('paymentpage/<str:name>/<str:price>', views.paymentpage, name='paymentpage'),
    path('paypage/<str:name>/<str:price>', views.paypage, name='paypage'),
    path('search/', views.search, name='search'),
    path('payments/', views.payments, name='payments'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('view_booking_details/', views.view_booking_details, name='view_booking_details'),
    path('admin_view_booking_appartment/', views.admin_view_booking_appartment, name='admin_view_booking_appartment'),
   
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
