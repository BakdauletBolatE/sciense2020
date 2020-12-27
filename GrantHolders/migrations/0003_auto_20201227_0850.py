# Generated by Django 3.1.4 on 2020-12-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrantHolders', '0002_auto_20201226_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grantholders',
            options={'verbose_name': 'Грант иегері', 'verbose_name_plural': 'Грант иегерлері'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Пән', 'verbose_name_plural': 'Пәндер'},
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Сабақтың аты'),
            preserve_default=False,
        ),
    ]
