from atexit import register
from django.contrib import admin

from blogs.models import Blog, BlogPost

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogPost)
