# Generated by Django 4.2.8 on 2023-12-08 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('ME', 'Mechanical Engineering'), ('SE', 'Software Engineering'), ('CE', 'Chemical Engineering')], max_length=255),
        ),
    ]
