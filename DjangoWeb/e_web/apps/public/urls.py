from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


app_name="public"
urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('gallery', views.gallery, name="gallery"),
    path('error_page', views.error_page, name="error_page"),
    path('properties_list', views.properties_list, name="properties_list"),
    path('properties_list/<int:pk>/', views.properties_list_retrieve, name="properties_list_retrieve"),
    path('create/', views.properties_list_create, name="create"),
    path('update-listing/<int:pk>/', views.properties_list_update, name="update listing"),
    path('delete-listing/<int:pk>/', views.deleteListing, name="delete-listing"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
