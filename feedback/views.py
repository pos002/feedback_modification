#from django.shortcuts import render
from .models import Feedback
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from .services.email import send_contact_email_message
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import FeedbackPasswordResetForm, FeedbackSetPasswordForm, FeedbackForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .services.utils import get_client_ip
from django.urls import reverse_lazy

class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'feedback_templates/feedback.html'
    extra_context = {'title': 'Контактная форма'}
    success_url = reverse_lazy('films:home')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.ip_address = get_client_ip(self.request)
        if self.request.user.is_authenticated:
            feedback.user = self.request.user
        feedback.save()
        send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address, feedback.user_id)
        return super().form_valid(form)
    # def get(self, request):
    #     return render(request, 'feedback_templates/feedback.html')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    #form_class = FeedbackPasswordResetForm
    template_name = 'feedback_templates/registration/password_reset_done.html'  # Укажите свой шаблон

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'feedback_templates/registration/password_reset_complete.html'  # Укажите свой шаблон
    success_url = reverse_lazy('login')


class CustomPasswordResetView(PasswordResetView):
    #form_class = FeedbackPasswordResetForm
    success_url = reverse_lazy('feedback:password_reset_done')
    template_name = 'feedback_templates/registration/password_reset.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = FeedbackSetPasswordForm
    success_url = reverse_lazy('feedback:password_reset_complete')
    template_name = 'feedback_templates/registration/password_reset_confirm.html'