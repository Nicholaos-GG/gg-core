# Generated by Django 4.2.7 on 2023-12-07 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_student_email_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
