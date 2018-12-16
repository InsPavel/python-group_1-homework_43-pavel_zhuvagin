# Generated by Django 2.1 on 2018-12-16 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20181216_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='commented_comment', to='webapp.Comment', verbose_name='Комментируемый комментарий'),
        ),
    ]