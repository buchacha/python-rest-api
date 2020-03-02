from django.shortcuts import render
 
from rest_framework import viewsets
from rest_framework.views import APIView, Response
from .models import Employee, Employer, HR
from .serializers import EmployeeSerializer, EmployerSerializer, HRSerializer
from django.core import serializers
import json
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
 
class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class HRViewSet(viewsets.ModelViewSet):
    queryset = HR.objects.all()
    serializer_class = HRSerializer

class CustomView(APIView):
    def get(self, request, format=None):
        return Response(json.loads(serializers.serialize("json", Employee.objects.all())))

    def post(self, request, format=None):
        print(request.data)
        return Response("ok")