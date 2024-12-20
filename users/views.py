from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserEditForm
from users.models import imagen
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('blog')  # Redirige al /blog después del inicio de sesión exitoso


def users_login(request):
    msg_login = ""
    if request.method == 'POST':
        # Validate the form
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/blog')  # Redirige al usuario a /blog
            else:
                msg_login = "Usuario o contraseña incorrectos"
        else:
            msg_login = "No posee una cuenta registrada"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def users_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')  # Redirige al login tras registrar
        else:
            messages.error(request, "Hubo un error al registrar el usuario. Por favor, revisa los datos ingresados.")
    else:
        form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form})   

@login_required
def users_profile(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES ,instance = usuario)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if imagen.objects.filter(user = usuario).exists():
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = imagen(user = usuario, imagen = miFormulario.cleaned_data.get('imagen'))  
                    avatar.save()
        miFormulario.save()
        return render(request, "users/profile.html", {"form": miFormulario})         
    else:
        miFormulario = UserEditForm(instance = usuario)
    return render(request, "users/profile.html", {"form": miFormulario})

def users_logout(request):
    return render(request, "users/logout.html")


def blog_index(request):
    return render(request, 'blog/index.html')
