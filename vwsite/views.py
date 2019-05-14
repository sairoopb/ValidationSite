from django.shortcuts import render
from .models import Credential
from .forms import UserForm, PasswordForm
from django.http import HttpResponse


def login(request):
    if (request.method == "GET"):
        form = UserForm()
        return render(request, 'vwsite/magic.html', {'form': form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse("Welcome " + form.cleaned_data["username"])
        else:
            return HttpResponse("Invalid")


def reset(request):
    if (request.method == "GET"):
        form = UserForm()
        pass_form = PasswordForm()
        return render(request, 'vwsite/fpassword.html', {'form': form,'pass_form': pass_form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            pass_form = PasswordForm(request.POST)
            if pass_form.is_valid():
                Credential.objects.filter(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"],
                    email=form.cleaned_data["email"]).update(
                        password=pass_form.cleaned_data["new_password"])
                return HttpResponse("Updated new password")        