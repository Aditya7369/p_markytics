from . import views
from django.urls import path
#app url
urlpatterns = [
    path('Show_User_form',views.Show_User_form,name="Show_User_form_url"),
    path('formsubmitpage_',views.formsubmitpage,name="formsubmitpage_url"),
    # path('display',views.displaydata),
    # path('edit/<int:id>',views.edit),
    # path('update/<int:id>',views.updatedata),
    # path('delete/<int:id>',views.deletedata)
]