from django.shortcuts import render, redirect
def example(request):
    return render(request, 'example.html')
