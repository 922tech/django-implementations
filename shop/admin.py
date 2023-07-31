from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', 'is_active')
    list_display_links = (('title',))
    list_display = ( 'title','price' ,'is_active', 'is_delete')
    list_editable = ( 'price','is_active', 'is_delete')


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
# admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
