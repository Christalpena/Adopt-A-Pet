from django import forms

class AdoptForm(forms.Form):
    person_name = forms.CharField(label='Your Name',required=True)
    person_last_name = forms.CharField(label='Last Name',required=True)
    id_number = forms.IntegerField(label='Id Number',required=True)
    date_of_birth = forms.DateField(label='Birth Date',required=True)
    street = forms.CharField(label='Street',required=True)
    city = forms.CharField(label='city',required=True)
    province = forms.CharField(label="Province",required=True)
    civil_status = forms.CharField(label='Civil Status',required=True)
    profession = forms.CharField(label='Profession',required=True)
    phone = forms.IntegerField(label='Phone Number',required=True)
    gmail = forms.EmailField(label='Gmail',required=True)




