from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return '%s, %s' % (self.title, self.author)
