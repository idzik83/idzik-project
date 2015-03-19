#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views.generic.base import RedirectView
from forms import UserForm
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponse, HttpRequest
from models import UserModel


# Create your views here.
class LoginView(FormView):
    template_name = "authform.html"
    success_url = '/'
    form_class = AuthenticationForm

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def logout(self):
        user = self.request.user
        if user.is_authenticated():
            auth.logout(request)
            return redirect('/')

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class RegistrationView(CreateView):
    form_class = UserForm
    success_url = '/'
    template_name = "registration.html"
    model = UserModel
    fields = '__all__'

    def form_valid(self, form):
        self.send(form)
        return super(RegistrationView, self).form_valid(form)


    def send(self, form):
        address = form.cleaned_data.get('email','').encode('utf-8')
        login = form.cleaned_data.get('login').encode('utf-8')
        msg = """Спасибо за регистрацию на сайте ...
        Ваш Логин: %s
        Ваш Пароль: %s
        Вернуться на сайт можете по ссылке .....""" % (login, address)
        return send_mail('Регистрация на сайте ....', msg, 'igor.idzikovsky@gmail.com', [address])
        
class UserCabinet(UpdateView):
    success_url = '/'
    form_class = UserForm
    model = UserModel
    fields = '__all__'
    template_name = "user_profile.html"
 
    def get_object(self, queryset=None):
        obj = UserModel.objects.get(id=self.kwargs['id'])
        return obj
