# Generated by Django 5.1.3 on 2024-11-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_student_age_remove_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]