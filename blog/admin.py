from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ('title', 'created')


@admin.register(Report)
class Report(admin.ModelAdmin):
    list_display = ('title', 'created')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'category')


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')


@admin.register(Submitted)
class SubmittedAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'sender')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('sender', 'created', 'post', 'video', 'photo')
