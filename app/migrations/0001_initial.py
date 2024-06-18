# Generated by Django 4.2.6 on 2024-06-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admission_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.CharField(default='', max_length=10)),
                ('dob', models.DateField(default='')),
                ('aadhaar', models.CharField(default='', max_length=12)),
                ('gender', models.CharField(default='', max_length=10)),
                ('education', models.CharField(default='', max_length=50)),
                ('doc_10th', models.FileField(blank=True, null=True, upload_to='documents')),
                ('doc_12th', models.FileField(blank=True, null=True, upload_to='documents')),
                ('doc_graduate', models.FileField(blank=True, null=True, upload_to='documents')),
                ('doc_postgraduate', models.FileField(blank=True, null=True, upload_to='documents')),
                ('course_name', models.CharField(default='', max_length=100)),
                ('address', models.TextField(default='')),
                ('state', models.CharField(default='', max_length=50)),
                ('district', models.CharField(default='', max_length=50)),
                ('pincode', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile_number', models.CharField(max_length=20)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField(default='', max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]