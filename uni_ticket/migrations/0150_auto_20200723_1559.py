# Generated by Django 3.0.7 on 2020-07-23 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0149_auto_20200723_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket2ticket',
            options={'ordering': ['subordinate_ticket', 'main_ticket'], 'verbose_name': 'Dipendenza Ticket', 'verbose_name_plural': 'Dipendenze Ticket'},
        ),
        migrations.RenameField(
            model_name='ticket2ticket',
            old_name='master_ticket',
            new_name='main_ticket',
        ),
        migrations.RenameField(
            model_name='ticket2ticket',
            old_name='slave_ticket',
            new_name='subordinate_ticket',
        ),
        migrations.AlterUniqueTogether(
            name='ticket2ticket',
            unique_together={('subordinate_ticket', 'main_ticket')},
        ),
    ]
