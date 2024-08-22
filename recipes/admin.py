from django.contrib import admin
from .models import Recipe, Comment, Bookmark
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'instructions']
    summernote_fields = ('description', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'author', 'text','email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'text', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_on')