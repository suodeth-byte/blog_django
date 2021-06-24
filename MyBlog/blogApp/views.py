from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Article, Author
from .forms import ArticleForm, CreateUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated
from django.views import generic, View
# from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy




@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'home.html'
    queryset = Article.objects.all()

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home.html', context)


@unauthenticated
def SignUpView(request):
    form = CreateUserForm({})
    print(form.is_bound)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            # form.save()
            username = form.data.get('username')
            email = form.data.get('email')
            password = form.data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            Author.objects.create(user=user)
            messages.success(request, 'Account was created for ' + username)


            return redirect('login')
    context = {'form': form}
    return render(request, 'sign_up.html', context)


@unauthenticated
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("IsAuthenticated", user.is_authenticated)
            messages.info(request, 'Username or Password is incorrect')
            return redirect('home')

    context = {}
    return render(request, 'login.html', context)


def LogOutView(request):
    logout(request)
    return redirect('login')


class ArticleCreateView(View):
    template_name = 'add_article.html'
    form = ArticleForm()
    queryset= Author.objects.all()

    def get_object(self):
        pass


    def get(self, request, *args, **kwargs):

        obj = self.request.user.username
        # form = ArticleForm()
        context = {'author': obj}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        print(user)

        author = Author.objects.filter(user=user).first()
        print(author)
        # form = ArticleForm(request.POST)
        title = self.request.POST.get('title')
        content = self.request.POST.get('content')
        Article.objects.create(title=title, content=content, author=author)
        # if form.is_valid():
        #     form.save()
            # print(form.cleaned_data)
            # print(form.clean)
        # dict = form.cleaned_data
        #
        # dict['author'] = author
        # form = dict
        # form.save()
        context = {'user': user, 'title': title, 'content': content}
        return render(request, self.template_name, context)


class ArticleDetailView(generic.DetailView):
    template_name = 'article_detail.html'
    queryset = Article.objects.all()
    # context_object_name = 'article'

    def article_detail_view(request, id):
        article = get_object_or_404(Article, id=id)
        return render(request, 'article_detail.html', context={'article': article})
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)


class ArticleUpdateView(generic.UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'article_update.html'


def articleListView(request):
    if request.method == 'GET':
        articles = Article.objects.filter(author__user=request.user)
        context = {'articles': articles}
        return render(request, 'article_list.html', context)


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article-list')


# class ArticleListView(generic.ListView):
#     model = Article
#     template_name = 'article_list.html'
#     context_object_name = 'articles'
#     queryset = Article.objects.all()
#
#     def get_queryset(self, request, *args, **kwargs):
#         articles = Article.objects.filter(author__user=self.request.user)
#         return self.articles


