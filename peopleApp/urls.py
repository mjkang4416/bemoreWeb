from django.urls import path
from .views import show_people

app_name = 'peopleApp'

urlpatterns = [
    path('', show_people, name='show_people'),
    #path('show_people/', show_people, name='show_people'),
]