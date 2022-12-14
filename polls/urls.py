from . import views
from django.urls import path

app_name="polls"
urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("<int:pk>/details/",views.DetailView.as_view(),name='detail'),
    path("<int:pk>/results/",views.ResultsView.as_view(),name='results'),
    path("<int:question_id>/voting/",views.voting,name='voting')
]