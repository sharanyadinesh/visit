from django.http import request
from django.shortcuts import render
from .models import Visit, Team, Company


# Create your views here.
def demo(request):
    obj=Visit.objects.all()
    team=Team.objects.all()
    comp=Company.objects.all()

    return render(request,'index.html',{'result':obj,'task':team,'firm':comp})