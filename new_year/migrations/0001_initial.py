# Generated by Django 5.0 on 2023-12-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewYearArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=70)),
                ('receiver_name', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('qr_code', models.CharField(max_length=200)),
            ],
        ),
    ]