# Generated by Django 3.0.8 on 2020-08-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200804_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]