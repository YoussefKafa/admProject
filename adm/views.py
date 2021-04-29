from django.shortcuts import render

# Create your views here.
from . import serializers
from rest_framework import generics, permissions, mixins, status
class admApiView(generics.CreateAPIView):
    serializer_class=serializers.PostSerializer

    def postTest(self, request):
            message= 'hello {0}'.format(age)
            return Response({'message':message})