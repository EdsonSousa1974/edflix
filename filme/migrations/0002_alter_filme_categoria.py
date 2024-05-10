# Generated by Django 4.2 on 2024-05-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ANALISE', 'Análise'), ('APRESENTACAO', 'Apresentação'), ('PROGRAMACAO', 'Programação'), ('COACH', 'Coaching'), ('OUTROS', 'Outros')], max_length=15),
        ),
    ]
