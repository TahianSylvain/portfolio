from django.shortcuts import render

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
    return render(request, './mainapp/index.html', status=200)

def faqs(request):
    return render(request, './mainapp/faqs.html', status=200)

def about(request): 
    return render(request, './mainapp/about.html', status=200)