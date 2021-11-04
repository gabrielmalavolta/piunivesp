from django.urls import path
from django.views.generic.base import TemplateResponseMixin
from . import views
 

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail") 

]

