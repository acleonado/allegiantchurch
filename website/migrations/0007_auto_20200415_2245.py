# Generated by Django 3.0.5 on 2020-04-15 22:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200415_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='desc',
            field=ckeditor.fields.RichTextField(blank=True, max_length=100),
        ),
    ]
