from django.shortcuts import render

# Create your views here.
def auth_login_view(request):
    return render(request, 'auth-login.html')

def register_view(request):
    return render(request, 'registro.html')
