from django.shortcuts import render,Http404, HttpResponse
from .models import Surf, Mega
import os
from django.conf import settings
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


@sync_to_async
def landing(request):
    file = Mega.objects.all()
    surfs = Surf.objects.all().order_by('-owner')
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
            rating = int(request.POST['ratingInput'])
        )
        
        print('You have 6-hours to put the right key, be careful !')
        key: str = "9"  ## available only for 6hours
        if "input_key" == str(input("insert your key")):
            new.save()
        else:
            new_owner.delete()
            print("Retry latter (30min)")
            
    return render(  request = request,
                    template_name = './mainapp/index.html', 
                    context = {"surfs": surfs, 'file': file},
                    status=200)

@sync_to_async
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exist(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.path.read(),
                content_type="application/cv")
            response['Content-Disposition']="inline;filename"+os.path.basename(file_path)
            return response
    raise Http404


def faqs(request):
    return render(request, './mainapp/faqs.html', status=200)


""" from django.shortcuts import render, redirect
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
