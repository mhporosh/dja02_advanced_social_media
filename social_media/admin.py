from django.contrib import admin
from .models import Post  # Import your models here

# Register your models here
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')  # Fields to display in the admin list view
    list_filter = ('created_at',)  # Add filters for these fields
    search_fields = ('content', 'user__username')  # Add search functionality for these fields