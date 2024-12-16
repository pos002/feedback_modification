# feedback/urls.py
from django.urls import path
from . import views
#from django.contrib.auth.views import LoginView
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView


app_name = 'feedback'
urlpatterns = [
    #path('login/', LoginView.as_view(), name='login'),
    path('', views.FeedbackView.as_view(), name='feedback'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]