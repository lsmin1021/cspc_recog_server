# Generated by Django 3.2.6 on 2021-08-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lastVisitTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]