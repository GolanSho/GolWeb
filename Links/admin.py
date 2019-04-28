from django.contrib import admin
from .models import Links


class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')


admin.site.register(Links, LinksAdmin)