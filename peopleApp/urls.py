from django.urls import path
from .views import show_people, profile

app_name = 'peopleApp'

urlpatterns = [
    path('show_people/', show_people, name='show_people'),
    path('profile/', profile, name='profile'),
    #path('profile/<str:id>/', profile, name='profile'),
]