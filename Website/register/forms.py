from django import forms

class NameForm(forms.Form):
    your_name=forms.CharField(label='Your name',max_length=200)
    your_roll=forms.IntegerField(label="Your Roll number")