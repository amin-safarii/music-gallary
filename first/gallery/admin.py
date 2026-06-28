from django.contrib import admin
from .models import Category, Artist, Post, SiteTheme


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'main_post', 'created_at')
    list_filter = ('category', 'main_post', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ('theme', 'updated_at')

    def has_add_permission(self, request):
        # فقط یه رکورد مجاز است
        return not SiteTheme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
