from django.contrib import admin

# Register your models here.
from . import models

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')


admin.site.register(models.Banners, BannerAdmin)
