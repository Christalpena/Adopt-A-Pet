from django import forms

class ServicesFroms(forms.Form):
    name = forms.CharField(label='Name', required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', required= True,widget=forms.TextInput(attrs={'class':'form-control'}))
    gmail = forms.EmailField(label='Gmail',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    date = forms.CharField(label='When do you want this service ?',required=True,widget=forms.TextInput(attrs={'class':'form-control',}))
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class':'form-control'}))