from django.shortcuts import render

# Create your views here.


def login(request):
    context ={'greeting': 'Welcome to spider'}
    return render(request, 'star/index.html', context)


def page(request):
    context ={'greeting': 'Welcome to spider'}
    return render(request, 'star/page.html', context)