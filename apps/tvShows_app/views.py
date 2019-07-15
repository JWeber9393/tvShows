from django.shortcuts import render, redirect
from . import models

def index(request):
    print('*'*100)
    print('showing all tv shows')
    return render(request, 'tvShows_app/index.html')

def new(request):
    print('*'*100)
    print('add a new show!!')

    context = {
        shows : new_show.objects.all()
    }

    return render(request, 'tvShows_app/new_show.html')

def create(request):
    print('*'*100)
    print('in the create method!!')

    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], releaseDate=request.POST['release'], description=request.POST['desc'])

    return redirect('/')