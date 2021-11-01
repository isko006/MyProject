"""mont3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from news import views
from accound import views as accound_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', views.NewsListAPIView.as_view()),
    path('api/v1/news/<int:pk>/', views.NewsFullListAPIView.as_view()),
    path('api/v1/register/', accound_views.RegisterAPIView.as_view()),
    path('api/v1/confirm/', accound_views.ConfirmAPIView.as_view()),
    path('api/v1/law/', views.LawListAPIView.as_view()),
    path('api/v1/law/<int:pk>/', views.LawFullListAPIView.as_view()),
    path('api/v1/publication/', views.PublicationListAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
