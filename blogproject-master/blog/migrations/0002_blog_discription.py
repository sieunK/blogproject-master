# Generated by Django 2.1.7 on 2019-02-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='discription',
            field=models.TextField(blank=True),
        ),
    ]
