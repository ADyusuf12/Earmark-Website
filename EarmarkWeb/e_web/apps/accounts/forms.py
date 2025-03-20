from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from .models import UserProfile

# Updated Registration Form
class RegisterForm(UserCreationForm):
    # Dynamically fetch group choices to keep them in sync with the database
    ACCOUNT_TYPE_CHOICES = [
        ('Customer', 'Customer'),
        ('Real Estate Agent', 'Real Estate Agent'),
        ('Real Estate Company', 'Real Estate Company'),
        ('Property Developer', 'Property Developer'),
        ('Property Owner', 'Property Owner'),
    ]

    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'account_type']

    def clean_account_type(self):
        # Validate that the selected account type exists in the database
        account_type = self.cleaned_data['account_type']
        if not Group.objects.filter(name=account_type).exists():
            raise forms.ValidationError(f"{account_type} is not a valid account type.")
        return account_type

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            # Assign the user to the selected group
            account_type = self.cleaned_data['account_type']
            try:
                group = Group.objects.get(name=account_type)
                group.user_set.add(user)

                # Assign group permissions to the user
                for perm in group.permissions.all():
                    user.user_permissions.add(perm)
            except Group.DoesNotExist:
                raise ValueError(f"The group '{account_type}' does not exist. Please ensure groups are correctly configured.")

        return user


# Updated Profile Form
class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']  # Exclude the user field since it's tied to the User model
