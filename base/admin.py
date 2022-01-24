from django.contrib import admin
from .models import Comment, Post
from django.shortcuts import render,redirect
from django.urls import path,reverse
from django import forms
from django.contrib import  messages
from django.http import  HttpResponseRedirect
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog database'


class TestPostAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.csv_view), ]
        return new_urls + urls

    def csv_view(self, request):
        if request.method == 'POST':
            csv_files = request.FILES['csv_upload']
            if not csv_files.name.endswith('.csv'):
                messages.warning(request,'The wrong file type was uploaded')
                print(request.path_info)
                return HttpResponseRedirect(request.path_info)
            file_data = csv_files.read().decode("utf-8")
            csv_data = file_data.split("\n")
            for i in csv_data:
                fields = i.split(',')
                if len(fields) == 3:
                    created = Post.objects.update_or_create(title=fields[0],author_id=fields[1],content=fields[2])
            url = reverse('admin:index')
            return HttpResponseRedirect(url)


        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', context=data)

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

admin.site.register(Post, TestPostAdmin)
admin.site.register(Comment)
