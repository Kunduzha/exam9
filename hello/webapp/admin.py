from django.contrib import admin

# Register your models here.
from webapp.models import Gallery, Albom


class GalleryAdmin(admin.ModelAdmin):
    gallery_display = ['image', 'caption', 'user', 'status']
    list_filter = ['created_at', 'caption']
    search_fields = ['caption']
    fields = ['image', 'caption', 'user']



admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Albom)