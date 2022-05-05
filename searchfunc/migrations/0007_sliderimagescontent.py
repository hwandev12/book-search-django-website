# Generated by Django 4.0.4 on 2022-05-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchfunc', '0006_rename_category_name_bookcategorymodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImagesContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_img', models.ImageField(upload_to='')),
                ('slider_header_content', models.CharField(max_length=100)),
                ('slider_text_content', models.TextField(max_length=400)),
            ],
            options={
                'verbose_name': 'Slider Content',
            },
        ),
    ]