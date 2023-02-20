from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blogger, Musician, Personality, Artist, Scientist, Project, Description


def main(request):
    data = {'data': [
        {'tag': 'blogger', 'data': Blogger.objects.all(), 'name': 'Блогери'},
        {'tag': 'musician', 'data': Musician.objects.all(), 'name': 'Музиканти'},
        {'tag': 'personality', 'data': Personality.objects.all(), 'name': 'Особистості'},
        {'tag': 'artist', 'data': Artist.objects.all(), 'name': 'Митці'},
        {'tag': 'scientist', 'data': Scientist.objects.all(), 'name': 'Науковці'},
        {'tag': 'project', 'data': Project.objects.all(), 'name': 'Проекти'}],

        'info': Description.objects.first()
    }

    return render(request, 'home.html', context=data)
