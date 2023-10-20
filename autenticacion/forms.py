from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_doctor', 'is_patient', 'is_admin']
        widgets = {
            'password': forms.PasswordInput(),
        }
