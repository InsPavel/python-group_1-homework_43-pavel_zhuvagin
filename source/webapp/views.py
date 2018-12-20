from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Article, User, Comment
from webapp.forms import SearchArticleForm, CreateArticleForm, UpdateArticleForm, CommentForm, UpdateCommentForm
from django.urls import reverse_lazy

class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = SearchArticleForm

    def get_queryset(self):
        article_name_text = self.request.GET.get('article_name_text')

        if article_name_text:
            return self.model.objects.filter(title__icontains=article_name_text) | self.model.objects.filter(text__icontains=article_name_text)
        else:
            return self.model.objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class FavoritesDetailView(DetailView):
    model = User
    template_name = 'favorites_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = UpdateArticleForm
    template_name = 'article_update.html'
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'
    success_url = reverse_lazy('article_list')

class CommentUpdateForm(UpdateView):
    model = Comment
    form_class = UpdateCommentForm
    template_name = 'comment_update.html'
    success_url = reverse_lazy('article_list')




