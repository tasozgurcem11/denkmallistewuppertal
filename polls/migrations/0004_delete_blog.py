# Generated by Django 3.0.6 on 2020-06-02 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
