# Generated by Django 4.0.7 on 2023-09-15 16:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('about', models.TextField()),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('srn', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=50)),
                ('is_recruiter', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.users')),
            ],
        ),
    ]
