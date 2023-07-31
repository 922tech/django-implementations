from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(BlogFile)
admin.site.register(BlogImage)
admin.site.register(Category)


class PostAdminModel(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('slug',)

