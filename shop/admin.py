from django.contrib import admin
from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', )
    # list_display_links = ('title', 'slug', 'price')
    list_filter = ('price', )
    search_fields = ('title', )
    prepopulated_fields = {"slug": ('title', )}


admin.site.register(Product, ProductAdmin)


