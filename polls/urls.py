from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/2/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/2/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/2/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]