# Generated by Django 4.1.4 on 2023-01-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('photo', models.ImageField(upload_to='HelpAppImages')),
                ('description', models.CharField(max_length=2000)),
                ('total_quantity', models.FloatField()),
                ('amount_collected', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': 'Donations',
            },
        ),
    ]
