import requests
import glob
import os

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print('index page requested...')
    context = {
        'view' : '100%'
    }
    return render(request, 'index.html', context)


def about_me(request):
    print('about me page requested...')
    response = requests.get('https://api.github.com/users/patrick-ware/repos')
    repos = response.json()
    repo_list = [
        [repo['name'], repo['html_url']]
        for repo in repos
    ]
    print(repo_list)
    context = {
        'view' : '50%',
        'repo_list' : repo_list,
    }
    return render(request, 'about_me.html', context)


def resume(request):
    print('resume page requested...')
    context = {
        'view' : '50%'
    }
    return render(request, 'resume.html', context)


def contact(request):
    print('contact page requested...')
    context = {
        'view' : '100%'
    }
    return render(request, 'contact.html', context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
