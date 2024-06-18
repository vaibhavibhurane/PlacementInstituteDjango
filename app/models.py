from django.db import models
from django.contrib.auth.models import User

from django.db import models


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(max_length=255, default="")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Admission(models.Model):
    admission_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    number = models.CharField(max_length=10, default="")
    dob = models.DateField(default="")
    aadhaar = models.CharField(max_length=12, default="")
    gender = models.CharField(max_length=10, default="")
    education = models.CharField(max_length=50, default="")
    doc_10th = models.FileField(upload_to='documents/', blank=True, null=True)
    doc_12th = models.FileField(upload_to='documents/', blank=True, null=True)
    doc_graduate = models.FileField(upload_to='documents/', blank=True, null=True)
    doc_postgraduate = models.FileField(upload_to='documents/', blank=True, null=True)
    course_name = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    state = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=50, default="")
    pincode = models.CharField(max_length=6, default="")

    def __str__(self):
        return self.name
