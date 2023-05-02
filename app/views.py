from django.shortcuts import render

# Create your views here.

from app.forms import *

from django.http import HttpResponse


def Registration(request):

    UFO=UserForm()
    PFO=ProfileForm()
    
    d={ 'UFO':UFO, 'PFO' : PFO }

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)

        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            # to add the user data into user_name coloumn in the profile form object

            NSPO=PFD.save(commit=False)
            NSPO.user_name=NSUO
            NSPO.save()

            return HttpResponse('Data IS valid')
        else:
            return HttpResponse('Data is Not valid')


    
    return render(request,'Registration.html',d)