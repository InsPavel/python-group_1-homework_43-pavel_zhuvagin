# Generated by Django 2.1 on 2018-12-16 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20181216_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, choices=[('terribly', 'Ужасно'), ('badly', 'Плохо'), ('normally', 'Нормально'), ('good', 'Хорошо'), ('perfectly', 'Отлично')], max_length=20, verbose_name='Оценка')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_grade', to='webapp.Article', verbose_name='Оценка для статьи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appreciated_by', to='webapp.User', verbose_name='Оценил(а)')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='commented_by', to='webapp.User', verbose_name='Прокомментировал(а)'),
        ),
    ]
