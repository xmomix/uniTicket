# Generated by Django 3.0.3 on 2020-03-25 07:03

from django.db import migrations, models
import organizational_area.models
import uni_ticket.validators


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0022_auto_20200313_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalstructure',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to=organizational_area.models._logo_upload, validators=[uni_ticket.validators.validate_file_size, uni_ticket.validators.validate_file_length]),
        ),
    ]
