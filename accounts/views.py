from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
import pickle
import datetime
import numpy as np
import json
# from .forms import NormalUserForm, Hotel, CabDriverForm
from .forms import NormalUserForm, HotelUserForm

model = pickle.load(
    open(r'C:\Users\HP\Downloads\HotelRBS\banglore_home_prices_model.pickle', 'rb'))
__locations = None
__data_columns = None

f = open(r'C:\Users\HP\Downloads\HotelRBS\columns.json')
__data_columns = json.loads(f.read())['data_columns']


def login_view(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']

        if username == "admin" and password == "admin":
            return redirect('accounts:admin')

        # Check NormalUser
        normal_user = authenticate(username=username, password=password)
        if normal_user is not None:
            login(request, normal_user)
            return redirect('appartment_user_view')

        normal_user2 = NormalUser.objects.filter(
            username=username, password=password).first()
        if normal_user2 is not None:
            login(request, normal_user2)
            request.session['id'] = normal_user2.user_id
            return redirect('accounts:appartment_user_view')

        # Check HotelOwner
        hotel_owner = HotelOwner.objects.filter(
            username=username, password=password).first()
        if hotel_owner is not None:
            login(request, hotel_owner)
            return redirect('accounts:hotel_owner_home')

        # Check CabDriver
        cab_driver = CabDriver.objects.filter(
            username=username, password=password).first()
        if cab_driver is not None:
            login(request, cab_driver)
            return redirect('cab_driver_home')

    return render(request, 'login.html')


def appartment_user_view(request):
    appartments = Appartment.objects.filter(status=1)   
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    today=datetime.datetime.now().date()
    appartmentbooking=appartment_booking.objects.filter(status=1)
    for i in appartmentbooking:
        if(i.start_date>=today) and (i.end_date>=today):
            # appart_name = Appartment.objects.get(ap_id=i.appartment_id)
            Appartment.objects.filter(ap_id=i.appartment_id).update(status=0)
        if(i.end_date < today):
            # appart_name = Appartment.objects.get(ap_id=i.appartment_id)
            Appartment.objects.filter(ap_id=i.appartment_id).update(status=1)
    return render(request, 'user_appartment.html', {'dis': dis, 'appartments': appartments})


def all_users(request):
    dis = NormalUser.objects.all()
    return render(request, 'all_user.html', {'dis': dis})


def home_view(request):
    __locations = __data_columns[3:]
    if request.method == 'POST':
        input_json = {
            "loca": request.POST['loc'],
            "area": request.POST['area'],
            "bhk": request.POST['bhk'],
            "bath": request.POST['bath']
        }

        result = get_estimated_price(input_json)

        if result > 100:
            result = round(result/100, 2)
            result = str(result) + ' Crore'
        else:
            result = str(result) + ' Lakhs'

        return render(request, 'result.html', {'result': result, 'input_json': input_json})

    return render(request, 'home.html', {'location': __locations})


def get_estimated_price(input_json):
    try:
        loc_index = __data_columns.index(input_json['loca'].lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = input_json['area']
    x[1] = input_json['bath']
    x[2] = input_json['bhk']
    if loc_index >= 0:
        x[loc_index] = 1
    result = round(model.predict([x])[0], 2)
    return result


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    appartments = Appartment.objects.all()
    return render(request, 'about.html', {'appartments': appartments})


def appartment(request):
    return render(request, 'appartment.html')


def normal_user_home(request):
    return render(request, 'home.html')


def hotel_owner_home(request):
    return render(request, 'hotelHome.html')


def cab_driver_home(request):
    return render(request, 'cabHome.html')


def booking(request, name):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    return render(request, 'booking.html',{'dis':dis,'appartments':appartments})
 
def bookings(request, name):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    return render(request, 'bookings.html',{'dis':dis,'appartments':appartments})

def edit(request, id):
    appartments = Appartment.objects.get(ap_id=id)
    return render(request, 'edit.html', {'appartments': appartments})

def adminappart(request):
    appartments = Appartment.objects.all()
    return render(request, 'adminappart.html', {'appartments': appartments})

from django.shortcuts import redirect

def delete(request, id):
    # Get the apartment object to delete
    apartment = Appartment.objects.get(ap_id=id)

    # Delete the apartment object
    apartment.delete()

    # Redirect the user to the apartment admin view
    return redirect('accounts:admin')



def editbtn(request, id):
    appartments = Appartment.objects.get(ap_id=id)
    if request.method == 'POST':
        apname = request.POST.get('apname')
        ptype = request.POST.get('ptype')
        adrs = request.POST.get('adrs')
        location = request.POST.get('location')
        zip = request.POST.get('zip')
        yr = request.POST.get('yr')
        ps = request.POST.get('ps')
        nb = request.POST.get('nb')
        nba = request.POST.get('nba')
        fur = request.POST.get('fur')
        ava = request.POST.get('ava')
        price = request.POST.get('price')
        prt = request.POST.get('prt')
        Appartment.objects.filter(ap_id=id).update(appartmentname=apname, propertytype=ptype, address=adrs, location=location,
                                                           zipcode=zip, year=yr, propertysize=ps, bedrooms=nb,
                                                           bathrooms=nba, furnishing=fur, availability=ava,
                                                           price=price, propdesc=prt)
    return redirect('accounts:admin')

def paymentpage(request,name,price):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    if request.method =="POST":
        st_date=request.POST.get('check-in-date')
        ed_date=request.POST.get('check-out-date')
    return render(request, 'payment.html',{'dis':dis,'appartment':appartments,'price':price,'st_date':st_date,'ed_date':ed_date})

def paypage(request,name,price):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    if request.method =="POST":
        st_date=request.POST.get('check-in-date')
    return render(request, 'payment copy.html',{'dis':dis,'appartment':appartments,'price':price,'st_date':st_date})


def payment(request,name):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    if request.method =="POST":
        price=request.POST.get('price')
        st_date=request.POST.get('start_date')
        ed_date=request.POST.get('end_date')
        ob=appartment_booking()
        ob.appartment_id=appartments.ap_id
        ob.appartment_name=appartments.appartmentname
        ob.user_id=dis.user_id
        ob.user=dis.username
        ob.price=price
        ob.start_date=st_date
        ob.end_date=ed_date
        ob.status=1
        ob.payment_status=1
        ob.save()
        return render(request, 'payments.html')

def pay(request,name):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    appartments = Appartment.objects.get(appartmentname=name)
    

    if request.method =="POST":
        price=request.POST.get('price')
        st_date=request.POST.get('start_date')
        ob=appartment_bookings()
        ob.appartment_id=appartments.ap_id
        ob.appartment_name=appartments.appartmentname
        ob.user_id=dis.user_id
        ob.user=dis.username
        ob.price=price
        ob.date=st_date
        ob.status=1
        ob.payment_status=1
        ob.save()
        Appartment.objects.filter(appartmentname=name).update(status=0)
        return render(request, 'payments.html')
    
def payments(request):
    return render(request, 'payments.html')


def logout_user(request):
    request.session.flush()
    return redirect('index')


def register_type(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'normal_user':
            return redirect('accounts:register_normal_user')
        elif user_type == 'hotel_owner':
            return redirect('accounts:register_hotel')
        elif user_type == 'cab_driver':
            return redirect('accounts:register_cab_driver')
        else:
            form = None
    else:
        form = None
    context = {
        'form': form
    }
    return render(request, 'registration_type.html', context)


def register_normal_user(request):
    form = NormalUserForm(request.POST or None)
    if form.is_valid():
        acc = NormalUser()
        acc.username = form.cleaned_data['firstname']
        acc.lastname = form.cleaned_data['lastname']
        acc.phone_num = form.cleaned_data['phone']
        acc.email = form.cleaned_data['email']
        acc.password = form.cleaned_data['password1']

        acc.save()
        return redirect('accounts:login')
    context = {
        'form': form
    }
    return render(request, 'register_normal_user.html', context)


def register_hotel_owner(request):
    form = HotelUserForm(request.POST or None)
    if form.is_valid():
        acc = HotelOwner()
        acc.username = form.cleaned_data['firstname']
        acc.lastname = form.cleaned_data['lastname']
        acc.email = form.cleaned_data['email']
        acc.password = form.cleaned_data['password1']

        acc.save()
        return redirect('accounts:login')
    context = {
        'form': form
    }
    return render(request, 'register_hotel_owner.html', context)


def admin(request):
    appartments = Appartment.objects.all()
    return render(request, 'admin.html', {'appartments': appartments})

def search(request):
    if request.method == 'POST':
        loc= request.POST.get('hotelloc')
        loca = Appartment.objects.filter(location=loc)
        return render(request, 'search.html', {'appartments': loca})

def appartments(request):
    if request.method == 'POST':
        apname = request.POST.get('apname')
        ptype = request.POST.get('ptype')
        adrs = request.POST.get('adrs')
        apname = request.POST.get('apname')
        location = request.POST.get('location')
        zip = request.POST.get('zip')
        yr = request.POST.get('yr')
        ps = request.POST.get('ps')
        nb = request.POST.get('nb')
        nba = request.POST.get('nba')
        fur = request.POST.get('fur')
        ava = request.POST.get('ava')
        rent = request.POST.get('rent')
        price = request.POST.get('price')
        img = request.FILES['image']
        prt = request.POST.get('prt')
        ob = Appartment()
        ob.appartmentname = apname
        ob.propertytype = ptype
        ob.address = adrs
        ob.location = location
        ob.zipcode = zip
        ob.year = yr
        ob.propertysize = ps
        ob.bedrooms = nb
        ob.bathrooms = nba
        ob.furnishing = fur
        ob.availability = ava
        ob.rent = rent
        ob.price = price
        ob.cimage = img
        ob.propdesc = prt
        ob.status=1
        ob.save()
    return redirect('accounts:admin')

def view_booking_details(request):
    id = request.session['id']
    dis = NormalUser.objects.get(user_id=id)
    booking=appartment_booking.objects.filter(user_id=id)
    appartment=Appartment.objects.all()
    return render(request,'view_booking.html',{'booking':booking,'appartment':appartment})

def admin_view_booking_appartment(request):
    if request.GET.get('start_date') and request.GET.get('end_date'):
        start_date = datetime.strptime(request.GET['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.GET['end_date'], '%Y-%m-%d').date()
        appartments = appartment_booking.objects.filter(start_date__lte=end_date, end_date__gte=start_date)
    else:
        appartments = appartment_booking.objects.all()
    return render(request,'viewbookingadmin.html',{'appartments':appartments})

    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            # Query the database to find all appartment bookings between start_date and end_date
            appartment_bookings = appartment_booking.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
            return render(request, 'search_results.html', {'appartment_bookings': appartment_bookings})
        else:
            # Render the search form again with an error message
            return render(request, 'search_form.html', {'error': 'Please enter both start date and end date.'})
