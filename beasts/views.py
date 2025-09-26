from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.

def home(request):
    return render(request, 'beasts/home.html')

from django.shortcuts import render, redirect
from .forms import ContestantForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContestantForm

def register_contestant(request):
    if request.method == 'POST':
        form = ContestantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Instead of Django messages, we pass a flag to the template
            return render(request, 'beasts/register.html', {'form': ContestantForm(), 'success': True})
    else:
        form = ContestantForm()

    return render(request, 'beasts/register.html', {'form': form})