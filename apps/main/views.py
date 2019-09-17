from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'main/home.html', context)

def about_page(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'main/about.html', context)

def login_page(request):
    context = {
        'title': 'Log in'
    }
    return render(request, 'main/login.html', context)

def join_beta(request):
    context = {
        'title': 'Log in'
    }
    return render(request, 'main/beta.html', context)

def pricing(request):
    context = {
        'title': 'Pricing'
    }
    return render(request, 'main/pricing.html', context)

def blog(request):
    context = {
        'title': 'Blog'
    }
    return render(request, 'main/blog.html', context)
