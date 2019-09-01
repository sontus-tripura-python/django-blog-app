from django.urls import path
from . import views
urlpatterns = [
     path('', views.post_created, name='post_created'),
     path('post/<int:pk>/', views.post_details, name='post_details'),
    ]
