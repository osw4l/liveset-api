from django.contrib import admin
from . import models
# Register your models here.


admin.site.site_header = 'LiveSet Admin'
admin.site.site_title = 'LiveSet Admin'
admin.site.index_title = 'LiveSet Admin'

COMMON_LIST_DISPLAY = ['id', 'name', 'order', 'file', 'active']


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = COMMON_LIST_DISPLAY


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = COMMON_LIST_DISPLAY

