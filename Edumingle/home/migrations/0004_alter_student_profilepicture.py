# Generated by Django 5.1.2 on 2024-11-08 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profilepicture',
            field=models.ImageField(blank=True, null=True, upload_to='profilepictures'),
        ),
    ]
