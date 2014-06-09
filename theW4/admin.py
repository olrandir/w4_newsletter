from django.contrib import admin

from models import Item, Newsletter, Language

admin.site.register(Item)
class NewsletterAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Language)