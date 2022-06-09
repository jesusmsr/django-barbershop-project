# Generated by Django 4.0.5 on 2022-06-09 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(max_length=8)),
                ('notes', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('booking_date', models.DateTimeField(default=None)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
