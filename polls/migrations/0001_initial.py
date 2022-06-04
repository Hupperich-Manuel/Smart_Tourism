# Generated by Django 3.2.5 on 2022-06-04 17:21

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
                ('building', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Building_name')),
                ('longitud', models.FloatField(verbose_name='Longitud')),
                ('latitud', models.FloatField(verbose_name='Latitud')),
                ('question_text1', models.IntegerField(verbose_name='Do you like places that service alcohol?')),
                ('question_text2', models.IntegerField(verbose_name='Do you enjoy trend places?')),
                ('question_text3', models.IntegerField(verbose_name='Do you enjoy crowded places?')),
                ('question_text4', models.IntegerField(verbose_name='Do you enjoy crowded places1?')),
                ('question_text5', models.IntegerField(verbose_name='Do you enjoy crowded places2?')),
                ('question_text6', models.IntegerField(verbose_name='Do you enjoy crowded places3?')),
                ('question_text7', models.IntegerField(verbose_name='Do you enjoy crowded places4?')),
                ('question_text8', models.IntegerField(verbose_name='Do you enjoy crowded places5?')),
                ('question_text9', models.IntegerField(verbose_name='Do you enjoy crowded places6?')),
                ('question_text10', models.IntegerField(verbose_name='Do you enjoy crowded places7?')),
                ('question_text11', models.IntegerField(verbose_name='Do you enjoy crowded places?8')),
                ('question_text12', models.IntegerField(verbose_name='Do you enjoy crowded places?9')),
                ('question_text13', models.IntegerField(verbose_name='Do you enjoy crowded places?10')),
                ('question_text14', models.IntegerField(verbose_name='Do you enjoy crowded places?11')),
                ('question_text15', models.IntegerField(verbose_name='Do you enjoy crowded places?12')),
                ('question_text16', models.IntegerField(verbose_name='Do you enjoy crowded places?13')),
                ('question_text17', models.IntegerField(verbose_name='Do you enjoy crowded places?14')),
                ('question_text18', models.IntegerField(verbose_name='Do you enjoy crowded places?15')),
                ('question_text19', models.IntegerField(verbose_name='Do you enjoy crowded places?16')),
                ('question_text20', models.IntegerField(verbose_name='Do you enjoy crowded places?17')),
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
                ('question_text4', models.IntegerField(verbose_name='Do you enjoy crowded places1?')),
                ('question_text5', models.IntegerField(verbose_name='Do you enjoy crowded places2?')),
                ('question_text6', models.IntegerField(verbose_name='Do you enjoy crowded places3?')),
                ('question_text7', models.IntegerField(verbose_name='Do you enjoy crowded places4?')),
                ('question_text8', models.IntegerField(verbose_name='Do you enjoy crowded places5?')),
                ('question_text9', models.IntegerField(verbose_name='Do you enjoy crowded places6?')),
                ('question_text10', models.IntegerField(verbose_name='Do you enjoy crowded places7?')),
                ('question_text11', models.IntegerField(verbose_name='Do you enjoy crowded places?8')),
                ('question_text12', models.IntegerField(verbose_name='Do you enjoy crowded places?9')),
                ('question_text13', models.IntegerField(verbose_name='Do you enjoy crowded places?10')),
                ('question_text14', models.IntegerField(verbose_name='Do you enjoy crowded places?11')),
                ('question_text15', models.IntegerField(verbose_name='Do you enjoy crowded places?12')),
                ('question_text16', models.IntegerField(verbose_name='Do you enjoy crowded places?13')),
                ('question_text17', models.IntegerField(verbose_name='Do you enjoy crowded places?14')),
                ('question_text18', models.IntegerField(verbose_name='Do you enjoy crowded places?15')),
                ('question_text19', models.IntegerField(verbose_name='Do you enjoy crowded places?16')),
                ('question_text20', models.IntegerField(verbose_name='Do you enjoy crowded places?17')),
                ('valuation', models.FloatField(default=0, verbose_name='Validation')),
                ('building', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
