from django.contrib import admin
from .models import Idea, Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'youtube_url']
    list_filter = ['status']

    def show_youtube_url(self, obj):
        return 'Tu będzie URL'
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']