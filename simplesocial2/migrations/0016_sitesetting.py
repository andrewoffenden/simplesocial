# Generated by Django 3.0.5 on 2020-10-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial2', '0015_auto_20201013_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
