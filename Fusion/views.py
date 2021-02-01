from django.http import HttpResponseRedirect
from django.shortcuts import render
from Fusion.forms import *


def example(request):
    return render(request, 'example.html')


def get_form_example(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExampleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any outher method) we'll create a blank form
    else:
        form = ExampleForm()
    return render(request, "form_test.html", {'form': form})


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
