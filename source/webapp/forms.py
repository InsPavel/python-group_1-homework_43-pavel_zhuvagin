from django import forms
from webapp.models import Article, Comment

class SearchArticleForm(forms.Form):
    article_name = forms.CharField(max_length=200, required=False, label="Название статьи")

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'article', 'comment', 'author']

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']