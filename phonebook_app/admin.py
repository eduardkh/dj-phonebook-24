from django.contrib import admin

from .models import Contact, PhoneNumber, EmailAddress


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline, EmailAddressInline]
    list_display = ('first_name', 'last_name', 'company', 'job_title')
    search_fields = ('first_name', 'last_name', 'company')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('contact', 'phone_type', 'number')
    search_fields = ('contact__first_name', 'contact__last_name', 'number')


@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('contact', 'email')
    search_fields = ('contact__first_name', 'contact__last_name', 'email')
