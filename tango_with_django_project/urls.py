from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    # above maps any urls starting
    # with rango/ to be handled by the
    # rango application
    url(r'^admin/', (admin.site.urls)),
    url(r'^about$', views.about, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
