from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import views

# Defining urls based on functions in views.py
urlpatterns = [
    path('', views.index),
    path('about-me/', views.about_me),
    path('resume/', views.resume),
    path('contact/', views.contact),
]

# Boilerplate to include static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
