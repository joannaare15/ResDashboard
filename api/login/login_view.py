from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def login_views(request):
    template_name = "auth-login.html"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # <- Esto ya funcionará porque importaste redirect
        else:
            return render(request, template_name, {
                'error': 'Credenciales inválidas',
                'username': username
            })

    return render(request, template_name)


#REGISTER
def register_view(request):
    template_name = "auth-register.html"
    return render(request, template_name)

#FORGET 
def forget_view(request):
    template_name = "auth-forgot-password.html"
    return render(request, template_name)

#LOGOUT
def logout_view(request):
    logout(request)
    return redirect('/login/')
