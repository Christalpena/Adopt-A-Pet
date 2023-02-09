from django.shortcuts import render,redirect
from .models import Animal,PersonInformation
from .forms import AdoptForm

# Create your views here.

def adopt(request):
    data = Animal.objects.all()
    return render(request,"AdoptPet/adopt.html",{'data':data})

def informationPage(request, id):
    data = Animal.objects.get(id = id)
    #print(data) 
    if data.vaccines == True:
        vaccines = 'Yes'

    else:
        vaccines = 'No'

    return render(request,'AdoptPet/informationPage.html',{'data':data,'vaccines':vaccines})

def adoptform(request, id):
    data = Animal.objects.filter(id= id)
    form = AdoptForm()
    if request.method == 'POST':
        #print(request.POST)
        form = AdoptForm(request.POST)

        if form.is_valid():
            name = Animal.objects.filter(id = id)
            for i in name:
                name = i
            person = PersonInformation()
            person.animal_name =(name)
            person.animal_id = (id)
            person.person_name = form.cleaned_data['person_name']
            person.person_last_name = form.cleaned_data['person_last_name']
            person.date_of_birth = form.cleaned_data['date_of_birth']
            person.id_number = form.cleaned_data['id_number']
            person.street = form.cleaned_data['street']
            person.city = form.cleaned_data['city']
            person.province = form.cleaned_data['province']
            person.profession = form.cleaned_data['profession']
            person.civil_status = form.cleaned_data['civil_status']
            person.phone = form.cleaned_data['phone']
            person.gmail = form.cleaned_data['gmail']


            try:
                person.save()
                return redirect("/AdoptAPet/?valid")
            except:
                return redirect("/AdoptAPet/?something_Went_Wron")
            

    return render(request,"AdoptPet/form.html",{'data':data,'form':form})


def dogs(request):
    data = Animal.objects.filter(kind= 6)
    return render(request,'AdoptPet/adopt.html',{'data':data})

def cats(request):
    data = Animal.objects.filter(kind= 7)
    return render(request,'AdoptPet/adopt.html',{'data':data})
