from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',views.obtain_auth_token),
    path('instagram/',include('instagram.urls')),
    path('twitter/', include('twitter.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)