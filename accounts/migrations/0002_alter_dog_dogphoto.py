# Generated by Django 3.2.13 on 2022-11-28 09:00

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dogphoto',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=''),
        ),
    ]