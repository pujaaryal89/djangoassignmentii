from django import forms
from .models import Blog,Author,Visitor


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    photo = forms.ImageField()

    class Meta:
        model = Visitor
        fields = ['username', 'email', 'password', 'confirm_password',
                  'mobile', 'name', 'address', 'photo']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

            
class BlogCreateForm(forms.ModelForm):
    
    class Meta:

        model = Blog
        fields = ['title', 'image','description']
     