# Generated by Django 3.2.13 on 2022-12-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deserted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindCd', models.CharField(max_length=100)),
                ('colorCd', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=30)),
                ('happenDt', models.DateField()),
                ('happenPlace', models.CharField(max_length=100)),
                ('noticeSdt', models.DateField()),
                ('noticeEdt', models.DateField()),
                ('processState', models.CharField(max_length=50)),
                ('sexCd', models.CharField(max_length=20)),
                ('neuterYn', models.CharField(max_length=20)),
                ('specialMark', models.CharField(max_length=200)),
                ('careNm', models.CharField(max_length=100)),
                ('careTel', models.CharField(max_length=100)),
                ('careAddr', models.CharField(max_length=100)),
                ('imageURL', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
