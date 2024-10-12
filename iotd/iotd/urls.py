# from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from images.views import home
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
