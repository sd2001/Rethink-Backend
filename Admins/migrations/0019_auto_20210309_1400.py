# Generated by Django 3.1.7 on 2021-03-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0018_auto_20210309_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
