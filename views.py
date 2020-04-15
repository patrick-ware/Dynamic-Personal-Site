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
    about_me_html = open('content/about_me.html').read()
    context = {
        'title' : 'about me',
        'view' : '050%',
        'content' : about_me_html,
    }
    return render(request, 'base.html', context)


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


pages = []

all_html_files = glob.glob("./content/*.html")

for page in all_html_files:
    rel_path = os.path.relpath(page)
    file_name = os.path.basename(page)
    name_only, extension = os.path.splitext(file_name)
    orig_dir = os.path.dirname(page)
    output_dir = './docs/'
    pages.append({
        'filename': rel_path,
        'url': name_only + extension,
        'output': os.path.join(output_dir, name_only + extension),
        'title': name_only,
        'view': '',
    })
