# Generated by Django 5.1.2 on 2024-11-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_student_password_student_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profilepicture',
            field=models.ImageField(blank=True, null=True, upload_to='Edumingle\\home\\profilepicturesofall'),
        ),
    ]
