from django.contrib import admin
from .models import Post, Category,Tag,Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","category","published_date")
    list_filter = ("category","published_date")    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user','created_date')
    search_fields = ('text','user_username','post_title')

# admin.site.register(Post)
# admin.site.register(Category)
#admin.site.register(Tag)

