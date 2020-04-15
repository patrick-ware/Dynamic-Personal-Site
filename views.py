import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index_html = open('content/index.html').read()
    context = {}
    return render(request, 'base.html', context)



def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'About Me',
        'pokemon': 'Under Construction',
    }
    return render(request, 'base.html', context)


def resume(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Resume',
        'pokemon': 'Under construction',
    }
    return render(request, 'base.html', context)


def contact(request):
    context = {
        'name': 'Contact Page',
        'pokemon': 'Under construction',
    }
    return render(request, 'base.html', context)



def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

