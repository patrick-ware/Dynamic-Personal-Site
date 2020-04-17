import requests
import glob
import os

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print('index page requested...')
    context = {}
    return render(request, 'index.html', context)


def about_me(request):
    print('about me page requested...')
    response = requests.get('https://api.github.com/users/patrick-ware/repos')
    repos = response.json()
    repo_list = [
        repo['name']
        for repo in repos
    ]
    context = {
        'github_repos' : repo_list,
    }
    return render(request, 'about_me.html', context)


def resume(request):
    print('resume page requested...')
    context = {}
    return render(request, 'resume.html', context)


def contact(request):
    print('contact page requested...')
    context = {}
    return render(request, 'contact.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
