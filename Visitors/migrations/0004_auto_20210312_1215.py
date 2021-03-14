# Generated by Django 3.1.7 on 2021-03-12 12:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Visitors', '0003_auto_20210311_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='app_id',
            new_name='patient_id',
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.UUIDField(default=uuid.UUID('90951dc9-e0d2-4337-89ad-83d6727c8dde'), editable=False, primary_key=True, serialize=False),
        ),
    ]