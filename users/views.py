from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import SignupForm,CustomLoginForm,EditProfileForm,EditPasswordForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from blog.forms import EditProfileInfoForm,CreateProfileForm
from django.views.generic import DetailView,UpdateView,CreateView
from blog.models import Profile

# Create your views here.

class ShowProfilePage(DetailView):
    model=Profile
    template_name='registration/userprofile.html';

class EditProfileView(UpdateView):
    model=Profile
    form_class = EditProfileInfoForm
    template_name= 'registration/editprofileinfo.html'   
    success_url=reverse_lazy('home')

class CreateProfileView(CreateView):
    model=Profile 
    template_name='registration/createprofile.html' 
    form_class=CreateProfileForm
    success_url=reverse_lazy('home')

class PasswordsChangeView(PasswordChangeView):
    form_class = EditPasswordForm
    template_name= 'registration/password.html'   
    success_url=reverse_lazy('passwordsuccess')

def PasswordsuccessView(request):
    return  render(request,'registration/passwordsuccess.html')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name= 'registration/editprofile.html'   
    success_url=reverse_lazy('home')
   
    def get_object(self):
        return self.request.user;
    



class CustomLoginView(LoginView):
    form_class=CustomLoginForm
    template_name= 'registration/signin.html'   
    success_url=reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class=SignupForm
    template_name= 'registration/register.html'   
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        subject, from_email, to = "Welcome On Board", "gagandeep.a24@gmail.com",self.request.POST['email']
        text_content = "<h1>Your Account Has Been Created</h1><p>Thanks & Regards</p>"
        html_content = "<h1>Your Account Has Been Created</h1><p>Thanks & Regards</p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            return super().form_valid(form)

