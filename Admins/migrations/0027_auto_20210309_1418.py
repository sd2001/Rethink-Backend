# Generated by Django 3.1.7 on 2021-03-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0026_auto_20210309_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='date_joined',
            field=models.TimeField(auto_now=True),
        ),
    ]
