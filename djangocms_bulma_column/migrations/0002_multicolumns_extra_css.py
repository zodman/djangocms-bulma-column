# Generated by Django 2.1.9 on 2019-06-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_bulma_column', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multicolumns',
            name='extra_css',
            field=models.CharField(default='extra', max_length=150, verbose_name='extra_css'),
            preserve_default=False,
        ),
    ]
