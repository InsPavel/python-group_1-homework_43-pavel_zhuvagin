# Generated by Django 2.1 on 2018-12-17 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20181216_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, to='webapp.Article', verbose_name='Избранное'),
        ),
    ]
