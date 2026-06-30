from django.db import models


class DonationMethod(models.Model):

    METHOD_CHOICES = (
        ('bank', 'Bank Account'),
        ('mobile', 'Mobile Money'),
        ('crypto', 'Cryptocurrency'),
        ('paypal', 'PayPal'),
        ('other', 'Other'),
    )

    method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES
    )

    title = models.CharField(max_length=200)

    account_name = models.CharField(
        max_length=255,
        blank=True
    )

    account_number = models.CharField(
        max_length=255,
        blank=True
    )

    bank_name = models.CharField(
        max_length=255,
        blank=True
    )

    instructions = models.TextField(blank=True)

    qr_code = models.ImageField(
        upload_to="donation_methods/",
        blank=True,
        null=True
    )

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Donation(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    donor_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    purpose = models.CharField(
        max_length=255,
        blank=True
    )

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"