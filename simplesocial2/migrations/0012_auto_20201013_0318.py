# Generated by Django 3.0.5 on 2020-10-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial2', '0011_auto_20201013_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_self': False}, related_name='_userprofile_friends_+', to='simplesocial2.UserProfile'),
        ),
    ]
