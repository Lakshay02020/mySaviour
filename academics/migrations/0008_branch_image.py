# Generated by Django 3.2.5 on 2023-02-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0007_wifi'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='image',
            field=models.ImageField(default='', upload_to='academics/images'),
        ),
    ]