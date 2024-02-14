# Generated by Django 5.0.2 on 2024-02-14 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_question_correct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'modulo'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'respuesta'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(max_length=200, verbose_name='Respuesta A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(max_length=200, verbose_name='Respuesta B'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Respuesta C'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Respuesta D'),
        ),
        migrations.AlterField(
            model_name='question',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Modulo'),
        ),
    ]
