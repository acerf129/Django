from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from restapp.serializers import CountrySerializer 
from restapp.models import Country
class TestView(APIView):
    
    permission_classes =(IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        qs = Country.objects.all()
        country1=qs.first()
        serializer = CountrySerializer(country1)
        # data = {
        #     'username':'admin',
        #     'years_active':10
        # }
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = CountrySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)