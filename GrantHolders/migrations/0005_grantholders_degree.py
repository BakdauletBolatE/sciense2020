# Generated by Django 3.1.4 on 2020-12-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrantHolders', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantholders',
            name='degree',
            field=models.CharField(choices=[('BK', 'Бакалавр'), ('MG', 'Магистратура'), ('DT', 'Доктарантура')], default='BK', max_length=2),
        ),
    ]
