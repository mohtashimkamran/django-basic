from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    creation="Mohtashim K"
    flatmates = [
        "Amit","BABA","Ankit"
    ]
    show_developer =True
    context={
        "creation" : creation,
        "flatmates" : flatmates
    }

    response = render(request,'HelloWorld\index.html',context)
    return response

def hello2(request):
    return render(request,'HelloWorld\hello2.html')