# Generated by Django 3.0.3 on 2020-03-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0076_auto_20200330_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='confirm_message_text',
            field=models.CharField(blank=True, help_text="Es: 'Hai correttamente confermato la tua partecipazione'. Apri e chiudi le parentesi graffe per inserire il codice del ticket. Lascia vuoto per usare il testo predefinito Ticket creato con successo con il codice {}", max_length=255, null=True, verbose_name='Messaggio di conferma'),
        ),
    ]
