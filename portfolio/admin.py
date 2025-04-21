from django.contrib import admin
from .models import Project, ContactMessage, SupportMessage, Education, Achievement, Post

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'image')  # Kategori eklendi
    search_fields = ('title', 'category')
    list_filter = ('category',)

    def image(self, obj):
        return f'<img src="{obj.image.url}" width="100" height="100" />'
    image.allow_tags = True

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'reason', 'created_at')
    search_fields = ('name', 'email', 'reason')
    list_filter = ('reason', 'created_at')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_year', 'end_year')
    search_fields = ('institution', 'degree')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    search_fields = ('title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}