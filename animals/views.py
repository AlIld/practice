from django.shortcuts import render

def home_screen_view(request):
    context = {}

    return render(request, 'home_page/page.html', context)

def cat_view(request):
    context = {}

    return render(request, '#', context)

def dog_view(request):
    context = {}

    return render(request, '#', context)

def fox_view(request):
    context = {}

    return render(request, '#', context)