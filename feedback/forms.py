from django import forms
# from dal import autocomplete
from .models import Feedback
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class FeedbackForm(forms.ModelForm):
    """
    Форма для отправки обратной связи
    """
    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }


class FeedbackPasswordResetForm(PasswordResetForm):
    reset_code = forms.UUIDField(label=_('Reset Code'))
    new_password1 = forms.CharField(
        label=_('New password'),
        widget=forms.PasswordInput,
        validators=[validate_password],
    )
    new_password2 = forms.CharField(
        label=_('New password confirmation'),
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned_data = super().clean()
        reset_code = cleaned_data.get('reset_code')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError(_("The two password fields didn't match."))

        try:
            self.feedback = Feedback.objects.get(reset_password_code=reset_code)
            if not self.feedback.is_reset_password_code_valid():
                raise forms.ValidationError(_("Invalid or expired reset code."))
        except Feedback.DoesNotExist:
            raise forms.ValidationError(_("Invalid or expired reset code."))

        return cleaned_data

    def save(self, commit=True):
        feedback = self.feedback
        feedback.user.set_password(self.cleaned_data['new_password1'])
        feedback.reset_password_code = None
        feedback.reset_password_code_expiration = None
        if commit:
            feedback.user.save()
            feedback.save()
        return feedback
    
    from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm
)

class FeedbackSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        validators=[validate_password],
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        widget=forms.PasswordInput,
    )

    