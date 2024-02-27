from django.urls import path
from .views import show_activity, upload
from django.conf.urls.static import static
from django.conf import settings

app_name = 'activity'


urlpatterns = [
    path('project/', show_activity, name='show_activity'),
    path('upload/', upload, name='upload'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)