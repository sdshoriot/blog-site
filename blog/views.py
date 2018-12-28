from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Chapter, Post, Profile


# home_page_view
def home(request):
	chapters = Chapter.objects.all()
	latest_post = Post.objects.latest_post()
	ctx = {'chapters':chapters, 'latest_post': latest_post}
	return render(request, 'blog/home.html', ctx)


# post_detail_page_view
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	first = Post.objects.filter(is_draft=False).first()
	last = Post.objects.filter(is_draft=False).last()
	ctx = {'post': post, 'first': first, 'last': last}
	return render(request, 'blog/post_detail.html', ctx)


# posts_of_chapter_page_view
def posts_of_chapter(request, pk):
	chapter = get_object_or_404(Chapter, pk=pk)
	post = Post.objects.filter(chapter=chapter, is_draft=False)
	ctx = {'chapter': chapter, 'post': post}
	return render(request, 'blog/posts_of_chapter.html', ctx)


# total_author_page_view
def total_author(request):
	authors = User.objects.all()
	return render(request, 'blog/total_author.html', {'authors': authors})


# posts_of_author_page_view
def posts_of_author(request, pk):
	author = get_object_or_404(User, pk=pk)
	post = Post.objects.filter(author=author, is_draft=False)
	ctx = {'author': author, 'post': post}
	return render(request, 'blog/posts_of_author.html', ctx)			