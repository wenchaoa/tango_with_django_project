from django.contrib import admin
from rango.models import Category, Page

#Chapter 5 Customise the admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
   
# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin) # Updated
admin.site.register(Page, PageAdmin)         # Updated
