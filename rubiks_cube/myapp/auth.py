from django.contrib.auth.forms import UserCreationForm
from .register_forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import re

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # login after register
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return JsonResponse({'success': True})

        data = {'success': False}
        if 'username' in form.errors: data['username'] = cleanhtml(form.errors['username'])
        if 'password1' in form.errors: data['password1'] = cleanhtml(form.errors['password1'])
        if 'password2' in form.errors: data['password2'] = cleanhtml(form.errors['password2'])
        if 'email' in form.errors: data['email'] = cleanhtml(form.errors['email'])
        if 'first_name' in form.errors: data['first_name'] = cleanhtml(form.errors['first_name'])
        if 'last_name' in form.errors: data['last_name'] = cleanhtml(form.errors['last_name'])

        return JsonResponse(data)

    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            login_user = authenticate(username=request.POST['username'], password=request.POST['password'])

            # login
            if login_user and login_user.is_active:
                login(request, login_user)
                return JsonResponse({'success': True})

        # return error
        return JsonResponse({'success': False, 'error': 'Your login details were incorrect.'})

    return render(request, 'login.html')

def cleanhtml(raw_html):
    try:
        r = re.compile('<.*?>')
        cleantext = re.sub(r, '', str(raw_html))
        return cleantext
    except:
        return False