"""admProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
sys.path.append('D:\\svu\\Term1\\ADMdatamining\\algorithm\\DjangoEx\\admProject\\admProject\\')
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf.urls import url, include
from naiveBayesCode import *

@api_view(['POST'])
def hello_world(request):
                body_unicode=request.body.decode('utf-8')
                body=json.loads(body_unicode)
                age=body['age']
                chestPain=body['chestPain']
                bloodPressure=body['bloodPressure']
                bloodSugar=body['bloodSugar']
                restElectro=body['restElectro']
                heartRate=body['heartRate']
                exerciceAngina=body['exerciceAngina']
                content=[int(age),int(chestPain),int(bloodPressure),int(bloodSugar),int(restElectro),int(heartRate),int(exerciceAngina)]
                return Response({ "result": predictRow(content)})
urlpatterns = [
  url(r'^getBayesResult/$', hello_world),
]
    