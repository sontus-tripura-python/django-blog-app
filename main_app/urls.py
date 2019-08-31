from django.urls import path
from . import views
urlpatterns = [
     path('', views.post_created, name='post_created'),
    ]
