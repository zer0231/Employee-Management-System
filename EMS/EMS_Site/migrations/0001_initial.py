# Generated by Django 4.1.5 on 2023-01-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employee_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=13)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.TextField()),
                ('status', models.BooleanField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'others')], max_length=1)),
                ('dob', models.DateField()),
                ('joining_date', models.DateField()),
                ('jobs', models.ManyToManyField(blank=True, to='EMS_Site.job')),
            ],
        ),
    ]
