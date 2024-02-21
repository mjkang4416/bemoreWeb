from django.urls import path
from .views import activity, upload
from django.conf.urls.static import static
from django.conf import settings

app_name = 'activity'


urlpatterns = [
    path('', activity, name='project'),
    path('upload/', upload, name='upload'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)