from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("add", views.add, name="add"),
    # path('', views.index, name='index'),
    # path('results/', views.results, name='results'),
    # path('about/', views.about, name='about'),
    # path('post_search/', views.post_search, name='post_search'),
]
