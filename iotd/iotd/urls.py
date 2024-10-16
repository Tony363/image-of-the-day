# from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from images.views import home
from django.urls import include, path, re_path
from django.urls import path
from images.views import ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView, ImageDeleteView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^$', home, name='home'),
    path('', ImageListView.as_view(), name='image_list'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('image/add/', ImageCreateView.as_view(), name='image_add'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image_update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
