from django.shortcuts import render
from django.shortcuts import render , HttpResponseRedirect , redirect ,HttpResponse
from .models import student
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import studentSerializer



class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
 

