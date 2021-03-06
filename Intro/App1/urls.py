from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('delete/<int:id>', views.delete_user),
    path('info/<int:id>', views.info),
]