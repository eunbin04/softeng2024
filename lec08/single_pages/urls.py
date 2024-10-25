from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('about_me/', views.about_page, name='about_me'),
    path("", views.landing_page, name='landing_page'),
    path("blog/", views.blog_list, name='blog_list'),
]