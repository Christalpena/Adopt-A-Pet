# Generated by Django 4.1.4 on 2023-01-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adopt', '0004_animal_gender_animal_height_animal_vaccines'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=30)),
                ('animal_id', models.IntegerField()),
                ('person_name', models.CharField(max_length=30)),
                ('person_last_name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField(max_length=30)),
                ('civil_status', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('gmail', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PersonInformation',
                'verbose_name_plural': 'PersonInformations',
            },
        ),
    ]
