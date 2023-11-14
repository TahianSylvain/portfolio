from django.shortcuts import render,Http404, HttpResponse
from .models import Surf, Mega
import os, random
from django.conf import settings
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from django.core.mail import send_mail

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
            owner = new_owner, 
            subject = str(request.POST['subject']),
            mess = str(request.POST['message']),
            rating = request.POST['ratingInput']
        )
                
        key = [random.randint(0, 9) for i in range(1, 10)]
        mail_subject = "Hi! Mail confirmation sent from Tahiana"
        message = f"""If you are new to our platform, please hit that key: {str(k for k in key)}"""
        to_email = new_owner.email
        
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # default
            recipient_list=[to_email],
            fail_silently=False
        )
        print('Smtp Made')
        
        print('You have 6-hours to put the right key, be careful !')
        if key == str(request.POST['key']):
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
