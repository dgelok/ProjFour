from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START W Z")

class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")


    ## validating using the CLEAN_ method
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError("Gotcha bot!")
    #     return botcatcher

    ## validation using django's built-in validators
    # this is the 'validators=[validators.MaxLengthValidator(0)])' on line 11

    ## custom validators
    # this is the check_for_z function, passed as a validator to the name form field
    # 'validators=[check_for_z]' is passed as an argument

    ## clean the entire form all at once


