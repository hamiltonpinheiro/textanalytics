from django.urls import include, path
from django.contrib import admin
from .api import router

urlpatterns = [   
    path('api/v1/', include(router.urls)),
    
]