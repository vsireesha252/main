from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siri(request):
    return render(request,'template.html')



# Create your views here.
def fun(request):
    return HttpResponse("Hello Python!!!")

