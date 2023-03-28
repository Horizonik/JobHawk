# Generated by Django 4.1.7 on 2023-03-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]