from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "avatar", "description"]


admin.site.register(UserProfile, UserProfileAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "cover"]


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title", "content", "category"]
    list_display = ["author", "title", "category", "content", "created_at"]


admin.site.register(Article, ArticleAdmin)
