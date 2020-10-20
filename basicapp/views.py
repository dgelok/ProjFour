from django.shortcuts import render
from . import forms
from basicapp.models import User
from basicapp.forms import NewUser
# Create your views here.

def index(req):
    return render(req, 'basicapp/index.html')

def form(req):
    form = forms.FormName()

    if req.method == 'POST':
        form = forms.FormName(req.POST)

        if form.is_valid():

            print("Validation success!")
            print("NAME: "+ form.cleaned_data['name'])
            print("email: "+ form.cleaned_data['email'])
            print("text: "+ form.cleaned_data['text'])

    return render(req, 'basicapp/form.html',{'form':form})

def users(req):

    form = NewUser()

    if req.method == "POST":
        form = NewUser(req.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(req)
        else:
            print("Error. Form is invalid")

    usersObj = User.objects.order_by('user_email')
    users = {"users": usersObj, "form": form}

    return render(req, 'basicapp/users.html', context=users)