# Generated by Django 3.1.7 on 2021-03-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0016_auto_20210309_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='Pb7f54', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
