from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de services
    path('services/', include('services.urls')),
    # Paths de blog
    path('blog/', include('blog.urls')),
    # Paths de pages
    path('page/', include('pages.urls')),
    # Paths de pages
    path('contact/', include('contact.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
