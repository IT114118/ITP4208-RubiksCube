from django.contrib.auth.forms import UserCreationForm
from .register_forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # login after register
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)

            return redirect('home')

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', { 'form': form })