from django import forms;
from .models import Post,Category,Profile,Comment;
types=Category.objects.all().values_list('category','category')
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','author','category','content','postimage')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.HiddenInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'},choices=types),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditProfileInfoForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('bio','phoneNo','website_url','facebook_url','instagram_url','twiiter_url','userimage')
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'phoneNo':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
            'twiiter_url':forms.TextInput(attrs={'class':'form-control'}),    
        }
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('user','bio','phoneNo','website_url','facebook_url','instagram_url','twiiter_url','userimage')
        widgets={
            'user':forms.HiddenInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'phoneNo':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
            'twiiter_url':forms.TextInput(attrs={'class':'form-control'}),    
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','category','content')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'},choices=types),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('first_name','last_name','comment','post')
        widgets={
            'post':forms.HiddenInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control'}),
        }