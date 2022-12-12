# Generated by Django 3.2.13 on 2022-12-09 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_petplace_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='petplace',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='petplace',
            name='imageURL',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='petplace',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='petplace',
            name='tel',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='petplace',
            name='url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='petplacebodyimage',
            name='bodyimage',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='petplaceslideimage',
            name='slideimage',
            field=models.CharField(max_length=500),
        ),
    ]