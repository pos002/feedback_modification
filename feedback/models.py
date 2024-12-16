from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django.core.mail import send_mail
from django.conf import settings
from films.models import MyModel
from django.urls import reverse

class Feedback(MyModel):
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Электронная почта (email)')
    reset_password_code = models.UUIDField(null=True, blank=True)
    reset_password_code_expiration = models.DateTimeField(null=True, blank=True)
    content = models.TextField(verbose_name='Содержимое письма')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True)
    user = models.ForeignKey('auth.User', verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    def is_reset_password_code_valid(self):
            if self.reset_password_code_expiration:
                return timezone.now() < self.reset_password_code_expiration
            return False

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'Вам письмо от {self.email} по теме: {self.subject}'