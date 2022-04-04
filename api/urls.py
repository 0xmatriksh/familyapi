from django.urls import path
from .views import FamilyView,FamilyCreateView

urlpatterns = [
    path('family',FamilyView.as_view(),name='home'),
    path('family/<pk>',FamilyCreateView.as_view(),name='create'),
]