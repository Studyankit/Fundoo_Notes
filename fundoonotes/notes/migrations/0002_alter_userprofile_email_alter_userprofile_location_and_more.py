# Generated by Django 4.0.4 on 2022-05-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
