# Generated by Django 4.0.2 on 2022-02-12 21:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('petfindr', '0004_pet_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact Phone Number', max_length=31),
        ),
    ]