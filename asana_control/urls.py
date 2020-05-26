from django.contrib import admin

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url('', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
