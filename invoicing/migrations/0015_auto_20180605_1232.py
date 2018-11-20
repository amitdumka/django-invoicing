# Generated by Django 2.0.6 on 2018-06-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0014_recalculate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'default_permissions': ('list', 'view', 'add', 'change', 'delete'), 'ordering': ('date_issue', 'sequence'), 'verbose_name': 'invoice', 'verbose_name_plural': 'invoices'},
        ),
    ]