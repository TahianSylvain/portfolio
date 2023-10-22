from django.shortcuts import render

def landing(request):
    return render(request, './mainapp/index.html', status=200)

def faqs(request):
    return render(request, './mainapp/faqs.html', status=200)

def about(request): 
    return render(request, './mainapp/about.html', status=200)