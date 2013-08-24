from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cc_myself = forms.BooleanField(required=False)
