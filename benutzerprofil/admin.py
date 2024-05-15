from django.contrib import admin

# Register your models here.

from .models import Post,Comment

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text', 'created_time']
    extra = 0



class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable','publish_date','created_time']  # id ist auto increment -> AUTO_FIELD-> setting.py

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','text','create_time']

admin.site.register(Post,PostAdmin)
# admin.site.register(Comment, CommentAdmin)
