# Generated by Django 3.1.7 on 2021-03-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0041_auto_20210310_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='P45664', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
