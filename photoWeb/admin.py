from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Cameraman)
class CameramanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'mark', 'created_at', ]
    search_fields = ['id', 'name', 'description', 'mark', 'created_at', ]
    list_filter = ['id', 'name', 'description', 'mark', 'created_at', ]
    ordering = ['-created_at', ]
    fields = ['id', 'name', 'description', 'mark', 'created_at', ]
    readonly_fields = ['id', 'created_at', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mark', 'created_at', ]
    search_fields = ['id', 'name', 'mark', 'created_at', ]
    list_filter = ['id', 'name', 'mark', 'created_at', ]
    ordering = ['-created_at', ]
    fields = ['id', 'name', 'mark', 'created_at', ]
    readonly_fields = ['id', 'created_at', ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'cameraman', 'title', 'imgLevel1', 'imgLevel2', 'imgLevel3', 'description',
                    'content', 'created_at', ]
    search_fields = ['id', 'category', 'cameraman', 'title', 'imgLevel1','imgLevel2','imgLevel3', 'description',
                     'content', 'created_at', ]
    list_filter = ['id', 'category', 'cameraman', 'title', 'imgLevel1','imgLevel2','imgLevel3', 'description',
                   'content', 'created_at',]
    ordering = ['-created_at', ]
    fields = ['id', 'category', 'cameraman', 'title', 'imgLevel1','imgLevel2','imgLevel3', 'description', 'content',
              'created_at', ]
    readonly_fields = ['id', 'created_at', ]


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message', 'created_at', ]
    search_fields = ['id', 'name', 'email', 'message', 'created_at', ]
    list_filter = ['id', 'name', 'email', 'message', 'created_at', ]
    ordering = ['-created_at', ]
    fields = ['id', 'name', 'email', 'message', 'created_at', ]
    readonly_fields = ['id', 'created_at', ]