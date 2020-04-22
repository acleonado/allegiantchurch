# Generated by Django 3.0.5 on 2020-04-16 00:23

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_delete_joinevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', phone_field.models.PhoneField(max_length=31)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Event')),
            ],
        ),
    ]