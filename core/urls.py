from cat_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index),
    path("cat_stats/", views.cat_stats),
   
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
