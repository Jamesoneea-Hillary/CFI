from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message'
        ]

    def clean_phone(self):

        phone = self.cleaned_data['phone']

        if len(phone) < 10:
            raise forms.ValidationError(
                "Enter a valid phone number."
            )

        return phone

    def clean_message(self):

        message = self.cleaned_data['message']

        if len(message) < 20:
            raise forms.ValidationError(
                "Message must be at least 20 characters."
            )

        return message