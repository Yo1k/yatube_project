from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    list_filter = ('pub_date',)
    search_fields = ('text',)


admin.site.register(Group)
admin.site.register(Post, PostAdmin)
