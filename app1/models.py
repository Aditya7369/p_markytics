from django.db import models

# Create your models here.
class User_model(models.Model):
    loc1=(
        ("CH","Corporate Headoffice"),
        ("OD","Operations Department"),
        ("WS","Work Station"),
        ("MD","Marketing Division"),
    )
    location1=models.CharField(max_length=50, choices=loc1)
    location2=models.TextField()
    decription=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    sev=(
        ("Mild","Mild"),
        ("Moderate","Moderate"),
        ("Severe","Severe"),
        ("Fatal","Fatal"),
    )
    severity=models.CharField(max_length=20, choices=sev)
    cause=models.TextField()
    actions=models.TextField()
    type_env=models.BooleanField()
    type_inju=models.BooleanField()
    type_property=models.BooleanField()
    type_vehicle=models.BooleanField()
    submitted=models.BooleanField()
    reported_by_id=models.IntegerField() 
