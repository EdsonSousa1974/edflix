# Generated by Django 4.2 on 2024-05-07 02:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_alter_filme_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='textolivre',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]