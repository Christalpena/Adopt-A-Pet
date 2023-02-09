from django.shortcuts import render,redirect
from .forms import ServicesFroms
from django.core.mail import EmailMessage
from .models import Services
# Create your views here.

def services(request):
    data = Services.objects.all()
    return render(request,"ServicesApp/services.html",{'data':data}) 

def modal(request,id):
    data = Services.objects.filter(id=id)
    form = ServicesFroms()
    if request.method == "POST":
        service = request.POST.get('service')
        form = ServicesFroms(data= request.POST)
        if form.is_valid():

    
            name = request.POST.get('name')
            last_name = request.POST.get('last_name')
            gmail = request.POST.get('gmail')
            service = request.POST.get('service')
            date = request.POST.get('date')
            message = request.POST.get('message')

            email = EmailMessage(
                'MESSAGE FROM DJANGO SERVICES APP (Adopt a pet)',
                'KIND OF SERVICE: {} \nDATE FOR THE SERVICE: {} \n{} \nBY: {} {}'.format(service,date,message,name,last_name),"",
                ['penaperezchristal@gmail.com'],reply_to=
                [gmail],
                )
            
            try:
                email.send()
                return redirect("/services/?valid")
            except:
                return redirect("/services/?something_Went_Wron")
    return render(request,"ServicesApp/form.html",{'data':data,'form':form}) 



    