from django import forms
from django.core.exceptions import ValidationError
from .models import Credential


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Credential
        fields = ('username','password','email')

    def clean(self):
        data = self.cleaned_data
        # print(data)
        if not Credential.objects.filter(username=data["username"],
                                         password=data["password"],
                                         email=data["email"]).exists():
            raise ValidationError("Invalid")
        return data


# def clean_email(self):
#     email = self.cleaned_data['email']
#     if not Credential.objects.filter(email=email).exists():
#         raise ValidationError("Email does not exists")
#     return email

# def clean_username(self):
#     username = self.cleaned_data['username']
#     if not Credential.objects.filter(username=username).exists():
#         raise ValidationError("Username does not exists")
#     return username

# def clean_password(self):
#     password = self.cleaned_data['password']
#     if not Credential.objects.filter(password=password).exists():
#         raise ValidationError("Password incorrect")
#     return password
