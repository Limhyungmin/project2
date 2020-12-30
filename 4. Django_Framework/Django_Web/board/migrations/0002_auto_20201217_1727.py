# Generated by Django 3.1.4 on 2020-12-17 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='contents',
            field=models.TextField(verbose_name='Contents'),
        ),
        migrations.AlterField(
            model_name='board',
            name='registered_dttm',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date_And_Time'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='User'),
        ),
    ]