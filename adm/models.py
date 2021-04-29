from django.db import models

# Create your models here.
class Post(models.Model):
    age=models.IntegerField
    chestPain=models.IntegerField
    bloodPressure=models.IntegerField
    bloodSugar=models.IntegerField
    restElectro=models.IntegerField
    heartRate=models.IntegerField
    exerciceAngina=models.IntegerField