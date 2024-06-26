from django.contrib import admin
from django.urls import path
from mainApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('maqola/<int:maqola_id>/', maqola, name='maqola'),
    path('aboout/', about, name='about'),
    path('talks/', TalksView.as_view(), name='talks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
