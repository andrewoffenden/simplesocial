# Generated by Django 3.0.5 on 2020-10-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial2', '0014_auto_20201013_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='simplesocial2.UserProfile'),
        ),
    ]
