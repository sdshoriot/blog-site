from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Chapter(models.Model):
	number = models.IntegerField()
	chapter_name = models.CharField(max_length=150)

	def __str__(self):
		return self.chapter_name


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	author_img = models.ImageField(upload_to='author_images', null=True, blank=True)
	author_name = models.CharField(max_length=50)
	author_description = models.TextField()
	author_facebook	= models.URLField(null=True, blank=True)
	author_twitter = models.URLField(null=True, blank=True)
	author_linkedin = models.URLField(null=True, blank=True)
	
	def __str__(self):
		return self.author_name

class PostManager(models.Manager):
	def latest_post(self):
		l_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:4]
		return l_post


class Post(models.Model):
	post_title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	post_serial_no = models.IntegerField()
	post_description = RichTextUploadingField()
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='post')
	category = models.ManyToManyField(Category)
	is_draft = models.BooleanField(default=False)

	objects = PostManager()
	
	def __str__(self):
		return self.post_title