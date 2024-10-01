from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.views import home_redirect




urlpatterns = [
    path('', home_redirect),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),  # URLs do app movies
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


