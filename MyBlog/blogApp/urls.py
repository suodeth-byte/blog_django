from django.urls import path

from django.urls import path
from .views import (
    home,
    SignUpView,
    LoginView,
    LogOutView,
    HomeView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    articleListView,
    ArticleDeleteView
)

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView, name='sign-up'),
    path('login/', LoginView, name='login'),
    path('logout/', LogOutView, name='logout'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('update/<str:pk>/', ArticleUpdateView.as_view(), name='article-update'),
    path('list/', articleListView, name='article-list'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='article-delete')


]
