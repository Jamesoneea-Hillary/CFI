from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import DonationMethod
from .forms import DonationForm


def donate_page(request):

    methods = DonationMethod.objects.filter(
        active=True
    )

    if request.method == "POST":

        form = DonationForm(request.POST)

        if form.is_valid():

            donation = form.save()

            # ----------------------------
            # Email to CFI
            # ----------------------------

            send_mail(

                subject=f"New Donation Pledge from {donation.donor_name}",

                message=f"""

A new donation has been submitted.

Donor Name:
{donation.donor_name}

Email:
{donation.email}

Phone:
{donation.phone}

Amount:
{donation.amount}

Purpose:
{donation.purpose}

Message:
{donation.message}

Status:
Pending

                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[
                    settings.EMAIL_HOST_USER
                ],

                fail_silently=False,

            )

            # ----------------------------
            # Thank You Email
            # ----------------------------

            send_mail(

                subject="Thank You for Supporting Community Focus International",

                message=f"""

Dear {donation.donor_name},

Thank you for your generous commitment to support Community Focus International.

We have successfully received your donation pledge.

Donation Amount:
{donation.amount}

Purpose:
{donation.purpose}

Our finance team will contact you shortly if any further information is required.

Your support enables us to continue empowering communities through education, health, livelihoods and sustainable development.

Thank you for making a difference.

Kind regards,

Community Focus International

                """,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[
                    donation.email
                ],

                fail_silently=False,

            )

            messages.success(

                request,

                "Thank you for your generosity. Your donation has been received successfully."

            )

            return redirect("donate")

    else:

        form = DonationForm()

    context = {

        "methods": methods,

        "form": form,

    }

    return render(

        request,

        "donations/donate.html",

        context,

    )

from django.db.models import Sum
from django.shortcuts import render
from .models import Donation

def donation_dashboard(request):
    data = (
        Donation.objects.values('created_at__month')
        .annotate(total=Sum('amount'))
        .order_by('created_at__month')
    )

    labels = [d['created_at__month'] for d in data]
    values = [d['total'] for d in data]

    return render(request, 'donations/dashboard.html', {
        'labels': labels,
        'values': values
    })