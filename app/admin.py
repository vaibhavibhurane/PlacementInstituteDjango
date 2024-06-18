from django.contrib import admin

# Register your models here.
from .models import Admission, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('msg_id', 'name', 'email', 'mobile_number', 'subject', 'message', 'created_date')
    search_fields = ('name', 'email', 'mobile_number', 'subject')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Admission)
