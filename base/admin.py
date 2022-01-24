from django.contrib import admin
from .models import Comment, Post
from django.shortcuts import render
from django.urls import path


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog database'


class TestPostAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.csv_view), ]
        return new_urls + urls

    def csv_view(self, request):
        return render(request, 'admin/csv_upload.html')

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

blog_site.register(Post, TestPostAdmin)

admin.site.register(Post,TestPostAdmin)
admin.site.register(Comment)
