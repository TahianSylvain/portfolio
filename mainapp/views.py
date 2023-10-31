from django.shortcuts import render
from .models import Surf
from django.contrib.auth.models import User


def landing(request):
    """from django.shortcuts import render, redirect
    from .models import MyModel
    from .forms import MyModelForm

    def submit_rating(request):
        if request.method == 'POST':
            form = MyModelForm(request.POST)
            if form.is_valid():
                form.save()
                # Redirect to a success page or return a response
                return redirect('success_page')
        else:
            form = MyModelForm()
        return render(request, 'your_template.html', {'form': form})
    """
    if request.method == "POST":
        new_owner = User.objects.create(
            email = str(request.POST['email']),
            password = '********',
            username = request.POST['name'],
        )
        new = Surf(
            owner = new_owner, #.username = request.POST['name']
            subject = str(request.POST['subject']),
            mess = str(request.POST['message']),
            rating = float(request.POST['ratingInput'])
        )
        new.save()
    return render(request, './mainapp/index.html', status=200)

def faqs(request):
    return render(request, './mainapp/faqs.html', status=200)

def about(request): 
    return render(request, './mainapp/about.html', status=200)