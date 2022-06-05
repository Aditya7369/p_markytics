from django.contrib import admin

# Register your models here.
from .models import User_model

@admin.register(User_model)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ["id","location1","location2","decription","date","time","severity","cause","actions","type_env","type_inju","type_property","type_vehicle","submitted","reported_by_id"]
