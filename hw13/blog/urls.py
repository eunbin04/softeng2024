from django.urls import path
from .views import PostList, PostDetail, category_posts, tag_page

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('blog/',PostList.as_view(), name='post_list'),
    path('blog/<int:pk>/',PostDetail.as_view(), name='post_detail'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
    path('tag/<slug:slug>/', tag_page, name='tag_page'),
]