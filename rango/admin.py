from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

#Chapter 5 Customise the admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
admin.site.register(Category)
admin.site.register(Page, PageAdmin)# Updated
