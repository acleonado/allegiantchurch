# Generated by Django 3.0.5 on 2020-04-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(default='events/default.jpg', upload_to='events'),
        ),
    ]
