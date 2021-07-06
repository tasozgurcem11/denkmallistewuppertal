# Generated by Django 3.0.6 on 2020-06-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200604_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='haus_kaufen_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='haus_mieten_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='wohnung_kaufen_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='wohnung_mieten_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
    ]