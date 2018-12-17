from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    favorites = models.ManyToManyField('Article', blank=True, verbose_name='Избранное')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='article_author', verbose_name='Автор')

    def __str__(self):
        return 'Статья: %s Автор: %s' % (self.title, self.author)


class Comment(models.Model):
    text = models.TextField(max_length=2000, verbose_name="Комментарий")
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name="commented_article", verbose_name="Комментируемая статья")
    comment = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="commented_comment", verbose_name="Комментируемый комментарий")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="commented_by", verbose_name="Прокомментировал(а)")

    def __str__(self):
        return 'Комментарий: %s Прокомментировал: %s' % (self.text, self.author)

class Rating(models.Model):
    RATING_TERRIBLY = 'terribly'
    RATING_BADLY = 'badly'
    RATING_NORMALLY = 'normally'
    RATING_GOOD = 'good'
    RATING_PERFECTLY = 'perfectly'

    STATUS_CHOICES = (
        (RATING_TERRIBLY, 'Ужасно'),
        (RATING_BADLY, 'Плохо'),
        (RATING_NORMALLY, 'Нормально'),
        (RATING_GOOD, 'Хорошо'),
        (RATING_PERFECTLY, 'Отлично')
    )

    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name="article_grade", verbose_name="Оценка для статьи")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="appreciated_by", verbose_name="Оценил(а)")
    rating = models.CharField(max_length=20, blank=True, choices=STATUS_CHOICES, verbose_name="Оценка")

    def __str__(self):
        return 'Оценка для статьи: %s' % self.article