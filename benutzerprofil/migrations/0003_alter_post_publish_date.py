# Generated by Django 5.0.6 on 2024-05-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benutzerprofil', '0002_alter_post_created_time_alter_post_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
