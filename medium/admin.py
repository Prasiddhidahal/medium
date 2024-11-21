from django.contrib import admin
from .models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'date_updated')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content')
    

admin.site.register(Post, Postadmin)


