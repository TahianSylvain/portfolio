from django.shortcuts import render

def landing(request):
    return render(request, './mainapp/index.html', status=200)