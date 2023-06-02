from django.shortcuts import render,HttpResponse
from myprogram.models import Email


def index(request):
    if request.method=="POST":
        e=Email()
        e.email=request.POST.get('email')
        e.save()
        return render(request,'myprogram/thnks.html')
    return render(request,'myprogram/index.html')



    



# Create your views here.
