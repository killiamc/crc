# Generated by Django 5.0.4 on 2024-05-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_newuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
