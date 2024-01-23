# Generated by Django 5.0.1 on 2024-01-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='year',
        ),
        migrations.AddField(
            model_name='skills',
            name='image',
            field=models.ImageField(null=True, upload_to='charts/', verbose_name='График'),
        ),
        migrations.AddField(
            model_name='skills',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название графика'),
        ),
    ]
