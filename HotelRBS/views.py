from django.shortcuts import render
from accounts.models import Appartment
from accounts.models import *
from django.http import HttpResponse
import datetime


def index(request):
    appartments = Appartment.objects.filter(status=1)
    today=datetime.datetime.now().date()
    appartmentbooking=appartment_booking.objects.filter(status=1)
    for i in appartmentbooking:
        if(i.start_date>=today) and (i.end_date>=today):
            appart_name = Appartment.objects.get(ap_id=i.appartment_id)
            Appartment.objects.filter(ap_id=i.appartment_id).update(status=0)
        if(i.end_date < today):
            # appart_name = Appartment.objects.get(ap_id=i.appartment_id)
            Appartment.objects.filter(ap_id=i.appartment_id).update(status=1)
    
    
    return render(request,'index.html', {'appartments': appartments})



