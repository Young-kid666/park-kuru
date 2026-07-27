from django.contrib import admin
from .models import ParkSlide, NewsArticle, Feedback, UserMark

# Настройка заголовков админ-панели
admin.site.site_header = "Парк Кура — Панель управления"
admin.site.site_title = "Парк Кура"
admin.site.index_title = "Управление контентом"


@admin.register(ParkSlide)
class ParkSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


@admin.register(UserMark)
class UserMarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'category')
    actions = ['approve_marks']

    @admin.action(description="Одобрить выбранные метки (опубликовать на карте)")
    def approve_marks(self, request, queryset):
        updated_count = queryset.update(is_approved=True)
        self.message_user(request, f"Успешно опубликовано меток: {updated_count}.")