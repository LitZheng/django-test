from django.urls import path

from . import views

app_name  = "app1"
"""urlpatterns = [
        path("", views.index, name="index"),
        path("user_list",views.user_list, name="user_list"),
        path("pic",views.pic, name="pic"),
        # ex: /polls/5/
        path("<int:question_id>/", views.detail, name="detail"),
        # ex: /polls/5/results/
        path("<int:question_id>/results/", views.results, name="results"),
        # ex: /polls/5/vote/
        path("<int:question_id>/vote/", views.vote, name="vote"),
    ]"""
urlpatterns = [
        path("user_list", views.user_list, name="user_list"),
        path("pic", views.pic, name="pic"),
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
]
