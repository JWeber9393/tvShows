from django.shortcuts import render

def index(request):
    print('*'*100)
    print('index route working')
    return render(request, 'tvShows_app/index.html')