# Generated by Django 3.0.8 on 2020-08-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200804_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rece',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rece',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rece',
            name='name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='rece',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]