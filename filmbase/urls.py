"""
URL configuration for filmbase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.conf.urls.static import static
#from feedback.views import FeedbackView 
#from feedback.views import PasswordResetView
from feedback.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
    path("", include("films.urls")),
    #path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", include("signup.urls")),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')), 
    path('login/', LoginView.as_view(), name='login'),
    path('password_reset/', CustomPasswordResetView.as_view(template_name='feedback_templates/registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(template_name='feedback_templates/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='feedback_templates/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(template_name='feedback_templates/registration/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
