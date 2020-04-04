from django.contrib import admin
from board.models import *

# Register your models here.


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body']
    fields = ['title', 'body', 'tags']

class CommentAdmin(admin.ModelAdmin):
    fields = ['title', 'advert']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    fields = ['title']


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)