# Generated by Django 3.1.7 on 2021-03-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0029_auto_20210309_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='P33862', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
