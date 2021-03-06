# Generated by Django 3.2.2 on 2021-05-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Haryana', 'Haryana'), ('Punjab', 'Punjab'), ('Chandigarh', 'Chandigarh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Bihar', 'Bihar'), ('Rajasthan', 'Rajasthan')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_img')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
