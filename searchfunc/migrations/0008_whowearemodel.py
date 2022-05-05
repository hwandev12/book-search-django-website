# Generated by Django 4.0.4 on 2022-05-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchfunc', '0007_sliderimagescontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoWeAreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_image', models.ImageField(upload_to='')),
                ('right_content_text', models.TextField(max_length=700)),
                ('right_content_1', models.CharField(max_length=60)),
                ('right_content_2', models.CharField(max_length=60)),
                ('right_content_3', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Who we are',
                'verbose_name_plural': 'Who we are page',
            },
        ),
    ]
