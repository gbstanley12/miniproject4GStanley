from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include(('polls.urls', 'polls'), namespace='polls')),
    path('', polls_views.home_view, name='home'),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)