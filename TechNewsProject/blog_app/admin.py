from django.contrib import admin
from .models import Post

# Register your models here - Old Method
#admin.site.register(Post)

#New way of registering a customized design
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #The line below directly allows the list display on the admin to have these orders
    list_display = ('title', 'publish', 'status','slug')

    #Implement a filter system to appear onto the right hand
    list_filter = ('status','created','publish','author')
    
    #Implement a search mechanism and determine what will be searched
    search_fields = ('title','body', 'created')
    
    #
    prepopulated_fields = {'slug': ('title',)}
    
    #Allow for the author to be displayed with a lookup instead of a drop down
    raw_id_fields = ('author',)
    
    #Allow for searching by the month
    date_hierarchy = 'publish'
    
    #Change the hierarchy to make the publish the default hierarchy
    ordering = ('status', 'publish')
    
    
    
