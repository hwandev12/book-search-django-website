# Generated by Django 4.0.4 on 2022-05-02 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchfunc', '0005_bookcategorymodel_bookcardsmodel_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcategorymodel',
            old_name='category_name',
            new_name='name',
        ),
    ]