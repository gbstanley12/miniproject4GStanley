from django.contrib import admin
from .models import Movie, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    fields = ['user', 'text', 'rating', 'created_at']
    readonly_fields = ['created_at']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'genre', 'director']
    search_fields = ['title', 'director', 'genre']
    list_filter = ['release_date', 'genre']
    fieldsets = [
        (None, {'fields': ['title', 'release_date', 'genre', 'director', 'image', 'poster']}),
    ]
    inlines = [ReviewInline]

admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'rating', 'created_at']
    search_fields = ['movie__title', 'user__username', 'text']
    list_filter = ['rating', 'created_at']
    fields = ['movie', 'user', 'text', 'rating', 'created_at']
    readonly_fields = ['created_at']

admin.site.register(Review, ReviewAdmin)
