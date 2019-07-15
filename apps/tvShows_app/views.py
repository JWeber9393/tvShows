from django.shortcuts import render, redirect
from .models import Show

def index(request):
    print('*'*100)
    print('showing all tv shows')

    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'tvShows_app/index.html', context)

def new(request):
    print('*'*100)
    print('add a new show!!')

    return render(request, 'tvShows_app/new_show.html')

def create(request):
    print('*'*100)
    print('in the create method!!')

    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], releaseDate=request.POST['release'], description=request.POST['desc'])

    return redirect(f'/shows/{new_show.id}')

def about(request, show_id):
    print('*'*100)
    print('in the about page!!')
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, 'tvShows_app/about.html', context)

def edit(request, show_id):
    print('*'*100)
    print('in the edit page!!')
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, f'tvShows_app/edit.html', context)


def update(request, show_id):
    show = Show.objects.get(id = show_id)
    show.title = request.POST['updateTitle']
    show.network = request.POST['updateNetwork']
    show.releaseDate = request.POST['updateRelease']
    show.description = request.POST['updateDesc']
    show.save()

    return redirect(f'/shows/{show.id}')


def destroy(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/shows')



