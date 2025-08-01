from django.contrib import admin
from . models import Category, Product
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'name', 'Category', 'price', 'stock', 'status')
    search_fields =("name",)
    list_filter = ("Category",)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.product_image:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.product_image.url)    
    image_preview.short_description = 'Image' 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

