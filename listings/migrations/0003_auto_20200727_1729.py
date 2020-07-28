# Generated by Django 2.1.1 on 2020-07-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200727_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
    ]
