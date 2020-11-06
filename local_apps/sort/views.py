from django.shortcuts import render

from rest_framework import viewsets

from . import models

from . import serializers

class DocumentViewset(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer

   




class DocumentClassificationViewset(viewsets.ModelViewSet):
    queryset = models.DocumentClassification.objects.all()
    serializer_class = serializers.DocumentClassificationSerializer

  
