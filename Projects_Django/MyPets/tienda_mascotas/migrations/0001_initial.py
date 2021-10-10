# Generated by Django 3.2.8 on 2021-10-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('id_country', models.IntegerField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Identification_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('id_user', models.IntegerField()),
                ('id_type', models.IntegerField()),
                ('id_race', models.IntegerField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('ip', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('abrev', models.CharField(max_length=4)),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('id_identification_type', models.IntegerField()),
                ('number_id', models.CharField(max_length=15)),
                ('id_city', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updatesd_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
    ]
