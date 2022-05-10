from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from searchfunc.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('searchfunc.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)