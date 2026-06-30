from django.contrib import admin
from .models import DonationMethod, Donation


@admin.register(DonationMethod)
class DonationMethodAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'method',
        'active'
    )

    list_filter = (
        'method',
        'active'
    )


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):

    list_display = (
        'donor_name',
        'amount',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'donor_name',
        'email'
    )