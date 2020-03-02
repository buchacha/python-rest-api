from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet, EmployerViewSet, HRViewSet, CustomView

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('employers', EmployerViewSet)
router.register('hrs', HRViewSet)

urlpatterns = [
    path('customview', CustomView.as_view()),
]

urlpatterns += router.urls