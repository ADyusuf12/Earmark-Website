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
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            group = self.cleaned_data['group']
            group.user_set.add(user)
            
            for perm in group.permissions.all():
                user.user_permissions.add(perm)
        return user
        
        

class ProfileForm(ModelForm):
    class Meta:
        model =  UserProfile
        fields = '__all__'
        exclude = ['user']
        