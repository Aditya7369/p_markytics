from django import forms
from .models import User_model
# from django.forms.fields import DateField,TimeField 
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget

class User_form(forms.ModelForm):
    class Meta:
        model=User_model
        fields="__all__"
        widgets={
            # 'date': forms.DateInput(format='%d/%m/%Y'), 
            # "date":DateField(),
            # "time":TimeField(),
            "date":AdminDateWidget(),
            "time":AdminTimeWidget(),
        }
