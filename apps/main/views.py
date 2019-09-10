from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'main/home.html')

def about_page(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'main/about.html')
