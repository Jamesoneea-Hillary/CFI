from django.db import models


class ContactInfo(models.Model):
    office_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    google_map_embed = models.TextField(
        blank=True,
        help_text="Paste Google Maps iframe embed code"
    )

    def __str__(self):
        return self.office_name
    
class OfficeHours(models.Model):

    weekday = models.CharField(max_length=50)

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    def __str__(self):
        return self.weekday


class ContactMessage(models.Model):

    STATUS_CHOICES = (
        ('new','New'),
        ('read','Read'),
        ('replied','Replied'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"