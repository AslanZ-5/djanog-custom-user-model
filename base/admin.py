from django.contrib import admin
from .models import Comment, Post


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog database'


class TestAdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='editor').exists():
            return True
        
        return False

    def has_view_permission(self, request, obj=None):
        return True
blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(Post, TestAdminPermissions)

admin.site.register(Post)
admin.site.register(Comment)
