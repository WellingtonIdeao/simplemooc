# Generated by Django 2.1.3 on 2018-12-19 19:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simplemooc', '0004_auto_20181129_1832'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enrollment',
            new_name='EnrollmentModel',
        ),
    ]