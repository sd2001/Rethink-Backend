# Generated by Django 3.1.7 on 2021-03-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0045_auto_20210310_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpractioner',
            name='id',
            field=models.CharField(default='Pc3ce5', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
