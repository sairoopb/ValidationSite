from django.shortcuts import render
from .models import Credential
from .forms import UserForm
from django.http import HttpResponse

def login(request):
    if(request.method == "GET"):
        form = UserForm()
        return render(request,'vwsite/magic.html',{'form':form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse("Welcome " + form.cleaned_data["username"])
        else:
            return HttpResponse("Invalid") 
