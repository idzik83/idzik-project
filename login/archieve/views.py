from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views.generic.base import RedirectView
from forms import UserForm
#delete
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Create your views here.
class LoginView(FormView):
    template_name = "authform.html"
    success_url = '/'
    form_class = AuthenticationForm

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

        def form_invalid(self, form):
            return super(LoginView, self).form_invalid(form)

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class RegistrationView(FormView):
    form_class = UserForm
    success_url = '/'
    template_name = "registration.html"

    def form_valid(self, form):
        return super(RegistrationView, self).form_valid(form)
