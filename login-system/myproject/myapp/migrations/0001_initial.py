# Generated by Django 3.2.8 on 2021-10-27 06:16

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]