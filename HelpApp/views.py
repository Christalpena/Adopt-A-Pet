from django.shortcuts import render,redirect
from .forms import HelpForm
from django.core.mail import EmailMessage
# Create your views here.

def help(request):
    form = HelpForm()
    if request.method =='POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            last_name = request.POST.get('last_name')
            gmail = request.POST.get('gmail')
            help = request.POST.get('kind_help')
            message = request.POST.get('message')
            
            email = EmailMessage(
                'MESSAGE FROM DJANGO HELP APP (Adopt a pet)',
                'KIND OF HELP: {} \n{} \nBY: {} {}'.format(help,message,name,last_name),"",
                ['penaperezchristal@gmail.com'],reply_to=
                [gmail],
            )

            try:
                email.send()
                return redirect ("/help/?valid")

            except:
                return redirect ("/help/?something_Went_Wron")


    return render(request,'HelpApp/help.html',{'form':form})
