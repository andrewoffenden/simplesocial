# Generated by Django 3.0.5 on 2020-10-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial2', '0021_auto_20201013_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplesocial2.NavBarLink')),
            ],
        ),
    ]
