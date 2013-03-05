from django.contrib import admin

from models import Item, Newsletter

admin.site.register(Item)
class NewsletterAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
admin.site.register(Newsletter, NewsletterAdmin)