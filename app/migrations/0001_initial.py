# Generated by Django 5.1.3 on 2024-12-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Murojatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tashriflar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('visit_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
