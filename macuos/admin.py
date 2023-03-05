from django.contrib import admin
from .models import Post, SmallCategory, BigCategory, Tag
 
admin.site.register(Post)
admin.site.register(SmallCategory)
admin.site.register(BigCategory)
admin.site.register(Tag)
