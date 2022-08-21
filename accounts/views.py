from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)


# Create your views here.
def login_view(request):
    context = {

    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            context.update({'error': 'invalid username or password'})
        else:
            login(request, user=user)
            return redirect('/articles')

    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')