# Generated by Django 3.1.4 on 2020-12-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GrantHolders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Грант иегерінің есімі')),
                ('age', models.DateField(verbose_name='Туылған жылы')),
                ('poster', models.ImageField(upload_to='graduate_img', verbose_name='Грант иегерінің суреті')),
                ('teacher', models.CharField(max_length=200, verbose_name='Ғылыми жетекшісі')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('project_name', models.CharField(max_length=255, verbose_name='Жобаның тақырыбы')),
                ('project_duration', models.CharField(max_length=255, verbose_name='Жобаның мерзімі')),
                ('purpose_project', models.CharField(max_length=255, verbose_name='Жобаның мақсаты')),
                ('ways_project', models.TextField(verbose_name='Жоба мақсатына жету жолдары')),
                ('expected_result', models.TextField(verbose_name='Күтілетін нәтиже')),
                ('novelty_scientific', models.TextField(verbose_name='Ғылыми жұмыстың жаңалығы')),
                ('graduate_year', models.IntegerField(default=0, verbose_name='Грант алған жылы')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GrantHolders.subject', verbose_name='Грант иегерінің пәні')),
            ],
        ),
    ]
