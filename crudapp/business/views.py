from django.shortcuts import render, redirect  
from business.forms import BusinessForm  
from business.models import Business  
# Create your views here.  
def create(request):  
    if request.method == "POST":  
        form = BusinessForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = BusinessForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    Businesss = Business.objects.all()  
    return render(request,"show.html",{'Businesss':Businesss})  
def edit(request, id):  
    Busines = Business.objects.get(bid=id)  
    return render(request,'edit.html', {'Business':Busines})  
def update(request, id):  
    Busines = Business.objects.get(bid=id)  
    form = BusinessForm(request.POST, instance = Busines)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'Business': Busines})  
def delete(request, id):  
    Busines = Business.objects.get(bid=id)  
    Busines.delete()  
    return redirect("/")  

# Create your views here.
