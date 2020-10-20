# Generated by Django 3.1.2 on 2020-10-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=64)),
                ('user_last_name', models.CharField(max_length=64)),
                ('user_email', models.EmailField(max_length=120, unique=True)),
            ],
        ),
    ]