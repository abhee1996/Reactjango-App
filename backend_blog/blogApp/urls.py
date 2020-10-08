
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/articles/', include('articles.api.urls')),
    path('core/', include('core.urls' ,namespace='core'))

    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

