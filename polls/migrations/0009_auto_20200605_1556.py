# Generated by Django 3.0.6 on 2020-06-05 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_formdata_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='first',
            new_name='vorname',
        ),
    ]