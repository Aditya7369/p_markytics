from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect   #redirect means like rollback
from .models import User_model
from .forms import User_form

def Show_User_form(request):    #save
    if request.method=="POST":   # hide
        data=User_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect("formsubmitpage_url")  #save    user register here automatic save information
    else:
        fm=User_form()   #form fields
        return render(request,'showform.html',{'form':fm})
def formsubmitpage(request):
    return render(request,"formsubmitpage.html") 