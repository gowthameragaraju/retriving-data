from django.shortcuts import render

# Create your views here.
from app.models import *
def topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'topics.html',d)


def webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'webpages.html',d)
    

