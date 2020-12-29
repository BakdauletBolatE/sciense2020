from django import forms

class LikeForm(forms.ModelForm):
    post = forms.CharField(label='Your name', max_length=100)
    user = forms.CharField()
