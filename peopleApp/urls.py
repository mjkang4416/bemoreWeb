from django.urls import path
from .views import people, profile

app_name = 'peopleApp'

urlpatterns = [
    path('people/', people, name='people'),
    path('profile/', profile, name='profile'),
    #path('profile/<str:id>/', profile, name='profile'),
]