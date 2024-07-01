from django.db import models

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PhoneNumber(models.Model):
    CONTACT_PHONE_TYPES = [
        ('mobile', 'Mobile'),
        ('office', 'Office'),
        ('home', 'Home'),
        ('other', 'Other'),
    ]

    contact = models.ForeignKey(
        Contact, related_name='phone_numbers', on_delete=models.CASCADE)
    phone_type = models.CharField(max_length=10, choices=CONTACT_PHONE_TYPES)
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.get_phone_type_display()}: {self.number}"


class EmailAddress(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='email_addresses', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email
