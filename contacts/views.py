from django.shortcuts import render
from django.http import JsonResponse

from .models import (
    ContactInfo,
    OfficeHours
)

from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings


def contact_page(request):

    info = ContactInfo.objects.first()

    office_hours = OfficeHours.objects.all()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            message = form.save()

            # Email to CFI

            send_mail(
                subject=f"New Contact Form: {message.subject}",
                message=f"""
Name: {message.name}

Email: {message.email}

Phone: {message.phone}

Message:

{message.message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    settings.EMAIL_HOST_USER
                ],
                fail_silently=False,
            )

            # Auto reply

            send_mail(
                subject="Thank You For Contacting Community Focus International",
                message=f"""
Dear {message.name},

Thank you for reaching out to Community Focus International.

We have received your message and one of our team members will respond shortly.

Best Regards,
Community Focus International
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[message.email],
                fail_silently=False,
            )

            return JsonResponse({
                'success': True,
                'message': 'Message sent successfully.'
            })

        return JsonResponse({
            'success': False,
            'errors': form.errors
        })

    context = {
        'info': info,
        'office_hours': office_hours,
        'form': ContactForm(),
    }

    return render(
        request,
        'contacts/contacts .html',
        context
    )

