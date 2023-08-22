from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
  
    
    context = {
     "FirstSection": FirstSection.objects.all(),
     "SecondSection":SecondSection.objects.all(),
     "ThirdSection":ThirdSection.objects.all(),
     "FourthSection":FourthSection.objects.all(),
     "FifthSection":FifthSection.objects.all(),
     "SixSection": SixSection.objects.all(),
     "Videos": Video.objects.all(),

    }
    return render(request , "index.html" , context)