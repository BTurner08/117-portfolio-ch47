from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': "Name"}))
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': "Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))
