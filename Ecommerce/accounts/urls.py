from django.urls import path
from .views import create_person, raed_person, delete_person, update_person

urlpatterns = [
    path('create/', create_person, name='create'),
    path('read/', raed_person, name='raed'),
    path('delete/', delete_person, name='delete'),
    path('update/', update_person, name='update'),
]
