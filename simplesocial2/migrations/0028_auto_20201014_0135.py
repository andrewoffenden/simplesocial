# Generated by Django 3.0.5 on 2020-10-14 01:35

from django.db import migrations, models
import simplesocial2.models


class Migration(migrations.Migration):

    dependencies = [
        ('simplesocial2', '0027_auto_20201014_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborationgrouppost',
            name='postpic',
            field=models.ImageField(blank=True, null=True, upload_to=simplesocial2.models.group_post_upload_dir),
        ),
        migrations.AlterField(
            model_name='collaborationgrouppostcomment',
            name='commentpic',
            field=models.ImageField(blank=True, null=True, upload_to=simplesocial2.models.group_comment_upload_dir),
        ),
        migrations.AlterField(
            model_name='navbarlink',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=simplesocial2.models.navbar_icon_upload_dir),
        ),
        migrations.AlterField(
            model_name='sitepost',
            name='postpic',
            field=models.ImageField(blank=True, null=True, upload_to=simplesocial2.models.site_post_upload_dir),
        ),
        migrations.AlterField(
            model_name='userpostcomment',
            name='commentpic',
            field=models.ImageField(blank=True, null=True, upload_to=simplesocial2.models.user_comment_upload_dir),
        ),
    ]