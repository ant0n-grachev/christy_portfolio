from django.urls import path
from . import views

urlpatterns = [
    path('', views.drawing_list, name='drawing_list'),
    path('<int:pk>/', views.drawing_detail, name='drawing_detail'),
]
