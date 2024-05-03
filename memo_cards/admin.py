from django.contrib import admin
from .models import Topic, Card, Item

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'modified_at')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
