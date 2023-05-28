from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from perfiles.models import Avatar


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form': formulario},
    )



def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)

            if user:
                login(request=request, user=user)
                return redirect('inicio')  # Redirect to the 'inicio' page
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'perfiles/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    try:
        avatar = request.user.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)

        if formulario.is_valid():
            avatar = formulario.save(commit=False)
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario(instance=avatar)
    return render(
        request=request,
        template_name="perfiles/formulario_avatar.html",
        context={'formulario': formulario},
    )