from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'base.html', context)


def about_me(request):
    context = {}
    return render(request, 'base.html', context)


def resume(request):
    context = {}
    return render(request, 'base.html', context)


def contact(request):
    context = {}
    return render(request, 'base.html', context)
