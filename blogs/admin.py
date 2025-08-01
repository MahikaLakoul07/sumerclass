from django.contrib import admin
from . models import BlogCategory, Blogs

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name')

class BlogsAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('name', 'description', 'goal', 'Category')

admin.site.register(BlogCategory)
admin.site.register(Blogs)
