from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from.models import UserProfile





class RegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'group']
        

class ProfileForm(ModelForm):
    class Meta:
        model =  UserProfile
        fields = '__all__'
        exclude = ['user']
        