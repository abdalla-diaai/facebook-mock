from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', post_list_and_create, name='index'),
    path('load_posts/<int:num_posts>/', load_posts, name='load_posts'),
    path('like_unlike_post/', like_unlike_post, name='like_unlike_post'),
    path('<int:pk>', view_post, name='view_post'),
    path('<int:pk>/data', post_details, name='post_details'),
    path('<int:pk>/update', update_post, name='update_post'),
    path('<int:pk>/delete', delete_post, name='delete_post'),

]