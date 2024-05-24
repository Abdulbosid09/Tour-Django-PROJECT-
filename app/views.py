

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Airways, Davlatlar
from .forms import DavlatlarForm



# Create your views here.
def index(request):
    categoriya = Category.objects.all()
    davlat = Davlatlar.objects.all()
    return render (request,'index.html', context={'cats':categoriya, 'davlat':davlat})

def davlat(request, id):
    category = get_object_or_404(Category, id=id)
    davlat = category.davlatlar.all()
    category = Category.objects.all()
    return render (request,'index.html', context={'category':category, 'davlat':davlat})


def airways(request):
    categoriya = Category.objects.all()
    return render (request,'airways.html', context={'cats':categoriya})


def create(request):
    form = DavlatlarForm()
    categoriya = Category.objects.all()
  


    if request.method == 'POST':
        form = DavlatlarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create.html', context={'form':form, 'cats':categoriya})
   


def update(request, id):
    updat = get_object_or_404(Davlatlar, id=id)
    categoriya = Category.objects.all()


    form = DavlatlarForm(instance=updat)

    if request.method == 'POST':
        form = DavlatlarForm(request.POST, request.FILES, instance=updat)  
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'create.html', context={'form':form,  'cats':categoriya})


def delete(request, id):
    delet = get_object_or_404(Davlatlar, id=id)
    delet.delete()
    return redirect('index')
    