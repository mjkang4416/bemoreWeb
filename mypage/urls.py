from django.urls import path
from . import views
app_name='mypage'

urlpatterns = [
    path('<str:username>/',views.mypage, name='mypage'),
    path('<str:username>/mypage_edit/',views.mypage_edit, name='mypage_edit'),
]