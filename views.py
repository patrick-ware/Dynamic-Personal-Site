import requests
import operator

from django.shortcuts import render


def index(request):
    print('index page requested...')
    context = {
        'view': '100%'
    }
    return render(request, 'index.html', context)


def about_me(request):
    print('about me page requested...')
    response = requests.get('https://api.github.com/users/patrick-ware/repos')
    repos = response.json()
    repo_info = [
        [repo['name'],
         repo['html_url'],
         repo['description'],
         repo['created_at'],
         ]
        for repo in repos
    ]
    sort_repo_info = sorted(repo_info, key=operator.itemgetter(3), reverse=True)
    context = {
        'view': '50%',
        'repo_info': sort_repo_info,
    }
    return render(request, 'about_me.html', context)


def resume(request):
    print('resume page requested...')
    context = {
        'view': '50%'
    }
    return render(request, 'resume.html', context)


def contact(request):
    print('contact page requested...')
    context = {
        'view': '100%'
    }
    return render(request, 'contact.html', context)
