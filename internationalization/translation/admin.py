# coding: utf-8


from django.contrib import admin

from .models import HelloText


class HelloTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', ]


admin.site.register(HelloText, HelloTextAdmin)