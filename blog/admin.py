from django.contrib import admin

from .models import Chapter, Category, Post, Profile


class ChapterAdmin(admin.ModelAdmin):
	list_display = ('id', 'chapter_name')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'is_draft', 'post_title', 'chapter')
	list_editable = ['is_draft']


admin.site.register(Chapter, ChapterAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(Post, PostAdmin),
admin.site.register(Profile),