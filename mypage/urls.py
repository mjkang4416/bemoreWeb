from django.urls import path
from . import views
app_name='mypage'

urlpatterns = [
    path('mypage/',views.mypage, name='mypage'),
    path('mypage_edit/',views.mypage_edit, name='mypage_edit'),
]