from django.contrib import admin
from .models import Comment, Post


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog database'


class TestAdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(Post, TestAdminPermissions)

admin.site.register(Post)
admin.site.register(Comment)
