# Generated by Django 3.2.5 on 2022-06-01 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('building', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Building_name')),
                ('longitud', models.FloatField(verbose_name='Longitud')),
                ('latitud', models.FloatField(verbose_name='Latitud')),
                ('question_text1', models.IntegerField(verbose_name='Do you like places that service alcohol?')),
                ('question_text2', models.IntegerField(verbose_name='Do you enjoy trend places?')),
                ('question_text3', models.IntegerField(verbose_name='Do you enjoy crowded places?')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surame')),
                ('question_text1', models.IntegerField(verbose_name='Do you like places that service alcohol?')),
                ('question_text2', models.IntegerField(verbose_name='Do you enjoy trend places?')),
                ('question_text3', models.IntegerField(verbose_name='Do you enjoy crowded places?')),
                ('valuation', models.FloatField(default=0, verbose_name='Validation')),
                ('building', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
