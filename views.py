import requests
import glob
import os

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print('index page requested...')
    index_html = open('content/index.html').read()
    context = {
        'title' : 'index',
        'view' : '100%',
        'content' : index_html,
    }
    return render(request, 'base.html', context)


def about_me(request):
    print('about me page requested...')
   # response = requests.get('https://api.github.com/users/patrick-ware/repos')
   # repos = response.json()
    context = {}
    return render(request, 'about_me.html', context)


def resume(request):
    print('resume page requested...')
    resume_html = open('content/resume.html').read()
    context = {
        'title' : 'resume',
        'view' : '050%',
        'content' : resume_html,
    }
    return render(request, 'base.html', context)


def contact(request):
    print('contact page requested...')
    contact_html = open('content/contact.html').read()
    context = {
        'title' : 'contact',
        'view' : '100%',
        'content' : contact_html,
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
