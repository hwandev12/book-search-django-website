# Generated by Django 4.0.4 on 2022-05-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchfunc', '0008_whowearemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EssentialsPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essential_header_text', models.CharField(max_length=200)),
                ('esential_paragraph', models.TextField(max_length=700)),
                ('essential_page_image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Essential',
                'verbose_name_plural': 'Essentials',
            },
        ),
    ]
