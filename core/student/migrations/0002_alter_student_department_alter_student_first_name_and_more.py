# Generated by Django 4.2.7 on 2023-11-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="department",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="student",
            name="phone_number",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="student",
            name="spiritual_title",
            field=models.CharField(max_length=255),
        ),
    ]