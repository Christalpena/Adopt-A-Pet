from django.shortcuts import render
from Adopt.models import Animal,Race

# Create your views here.

def main(request):

    return render(request,'PetsWebPage/PetsPage.html')


def searchinf(request):
    queryset = request.GET.get("search")
    data = Animal.objects.filter(race__race__icontains = queryset)
    print(data)

    return render(request,'./AdoptPet/adopt.html',{'data':data})
