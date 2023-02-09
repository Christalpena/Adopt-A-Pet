from django import forms
help_choices = [
    ('Donate Food','Donate Food'),
    ('Be a Volunteer','Be a Volunteer'),
    ('Sponsor an Abandoned Animal','Sponsor an Abandoned Animal'),
    ('A Home For Animals','A Home For Animals')
]
class HelpForm(forms.Form):
    name= forms.CharField(label='Name',required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name =forms.CharField(label="Last Name",required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gmail = forms.EmailField(label="Gmail",required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    kind_help = forms.MultipleChoiceField(label='Help',required=True,widget=forms.CheckboxSelectMultiple,choices=help_choices)
    message = forms.CharField(label="Message",required=True, widget=forms.Textarea(attrs={'class': 'form-control',}))
