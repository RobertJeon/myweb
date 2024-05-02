from django.contrib import admin
from .models import Post
from .models import Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Post, PostAdmin)