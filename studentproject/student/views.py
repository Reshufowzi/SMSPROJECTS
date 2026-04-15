from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Placementcell
from .forms import SearchForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    x = {
        'NAME': "ANU",
        'AGE': 32,
        'PLACE': 'CHENNAI'
    }
    return render(request,'home.html',x)
def about(request):
    numbers = {
        'number1': -10,
    }
    return render(request,'about.html',numbers)

def department(request):
    dict_dept={
        'dept' : Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def placementcell(request):
    dict_place = {
        'placementcell' : Placementcell.objects.all()
    }
    return render(request,'placementcell.html',dict_place)


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()

    form = SearchForm
    dict_form = {
        'form': form
    }
    return render(request, 'search.html', dict_form)

def contact(request):
    numbers = {
        'number1' : [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,'contact.html',numbers)