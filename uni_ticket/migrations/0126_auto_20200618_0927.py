# Generated by Django 3.0.7 on 2020-06-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0125_auto_20200618_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closing_state',
            field=models.IntegerField(blank=True, choices=[(-1, 'Rifiutata'), (0, 'Non risolta'), (1, 'Risolta con successo'), (2, 'Non definia')], null=True),
        ),
    ]
