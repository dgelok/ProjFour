from django.shortcuts import render
from . import forms
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