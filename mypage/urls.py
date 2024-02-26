from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='mypage'

urlpatterns = [
    path('<str:username>/',views.mypage, name='mypage'),
    path('<str:username>/mypage_edit/',views.mypage_edit, name='mypage_edit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)