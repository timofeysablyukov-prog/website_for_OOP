from django import forms
class Form(forms.Form):
    field = forms.CharField(widget=forms.Textarea)