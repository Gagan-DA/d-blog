from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm;
from django.contrib.auth.models import User;
from django import forms;

class EditPasswordForm(PasswordChangeForm):
    old_password=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        fields=('old_password','new_password1','new_password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['password'].widget.attrs['class']="form-control"


class SignupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password2'].widget.attrs['class']="form-control"


class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(max_length=255, disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=255, disabled=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model= User
        fields=('username','email','first_name','last_name','email','date_joined','last_login')

