# Generated by Django 4.0.4 on 2022-05-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchfunc', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
