from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

from.models import Producto

def productos(request):
    producto_lista = Producto.objects.all()
    return render(request, 'productos.html', {'productos': producto_lista})


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

      
        if not username or not password:
            messages.error(request, "Por favor, ingresa el usuario y la contraseña.")
            return render(request, 'login.html')

        try:
           
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
          
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
               
                login(request, authenticated_user)
            
                return redirect('productos')
            else:
                
                messages.error(request, "Contraseña incorrecta.")
        else:
            
            messages.error(request, "El usuario no está registrado.")
    
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está registrado.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, "¡Registro exitoso! Has iniciado sesión.")
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'register.html')


def contactenos(request):
    return render(request, 'contactenos.html')






    

