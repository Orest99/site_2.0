# Generated by Django 5.1.7 on 2025-04-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_electro', '0021_remove_components_component_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='component_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип компонента'),
        ),
    ]
