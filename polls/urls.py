from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    re_path(r'.*login/', auth_views.login, {'template_name': 'polls/login.html'}, name='login'),
    path('signup/',views.signup, name='signup'),
]