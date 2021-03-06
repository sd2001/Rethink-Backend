# Generated by Django 3.1.7 on 2021-03-12 12:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Visitors', '0006_auto_20210312_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentverify',
            old_name='pid',
            new_name='patient_id',
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.UUIDField(default=uuid.UUID('373d46d3-2d16-466e-8ead-af0a750ea470'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b64cbd48-c18b-4a76-b607-24ae55fe460e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
