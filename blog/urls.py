from django.urls import include, path
from .views import home, post_detail, posts_of_chapter, total_author, posts_of_author


urlpatterns = [
	path('', home, name='home'),
    path('post_detail/<int:pk>', post_detail, name='post_detail'),
    path('posts_of_chapter/<int:pk>', posts_of_chapter, name='posts_of_chapter'),
    path('total_author/', total_author, name='total_author'),
    path('posts_of_author/<int:pk>', posts_of_author, name='posts_of_author'),
]