from django.http import HttpResponseRedirect
from django.shortcuts import render
from Fusion.forms import *




def get_vendor_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VendorRegistraionForm(request.POST)
        # check whether it's valid:
        print(form.errors)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            registration = form.save(commit=False)
            registration.save()
            return HttpResponseRedirect('/thank_you/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VendorRegistraionForm()
    return render(request, "vendor_form.html", {'form': form})


def get_small_business_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SmallBusinessRegistraionForm(request.POST)
        # check whether it's valid:
        print(form.errors)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            registration = form.save(commit=False)
            registration.save()
            return HttpResponseRedirect('/thank_you/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SmallBusinessRegistraionForm()
    return render(request, "small_business_form.html", {'form': form})

def thank_you_vendor(request):
    return render(request, "thank_you_vendor.html")

def thank_you_business(request):
    return render(request, "thank_you_business.html")

def get_home(request):
    return render(request, "home.html")

def get_about(request):
    return render(request, "about.html")

def get_benefits(request):
    return render(request, "benefits.html")

