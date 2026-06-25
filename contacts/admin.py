from django.contrib import admin
from .models import ContactInfo, ContactMessage, OfficeHours


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('office_name', 'phone', 'email')

@admin.register(OfficeHours)
class OfficeHoursAdmin(admin.ModelAdmin):
    list_display = (
        'weekday',
        'opening_time',
        'closing_time'
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'status',
        'submitted_at'
    )

    list_filter = (
        'status',
        'submitted_at'
    )

    search_fields = (
        'name',
        'email',
        'phone'
    )