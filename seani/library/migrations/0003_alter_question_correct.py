# Generated by Django 5.0.2 on 2024-02-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_question_text_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(max_length=5, verbose_name='Respuesta Correcta'),
        ),
    ]