from django.conf import settings
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .views import SavedListingsView


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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', success_url=reverse_lazy('public:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', success_url=reverse_lazy('public:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('save-listing/<int:pk>/', views.save_listing_view, name='save_listing'),
    path('saved_listings/', login_required(SavedListingsView.as_view()), name='saved_listings'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
