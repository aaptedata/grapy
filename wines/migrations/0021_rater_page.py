# Generated by Django 2.0.2 on 2018-06-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0020_auto_20180614_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='page',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
