from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'adoption_homepage.html', context)()


def about_me(request):
    return render(request, 'adoption_homepage.html', context)


def resume(request)
    return render(request, 'adoption_homepage.html', context)


def contact(request)
    return render(request, 'adoption_homepage.html', context)
