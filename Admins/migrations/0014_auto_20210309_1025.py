# Generated by Django 3.1.7 on 2021-03-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0013_auto_20210309_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='Pb8510', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]