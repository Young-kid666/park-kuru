from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Текст обращения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения граждан"
        ordering = ['-created_at']

    def __str__(self):
        return f"Обращение от {self.name} ({self.email})"


class ParkSlide(models.Model):
    title = models.CharField(max_length=150, verbose_name="Альтернативный текст (alt)")
    description = models.CharField(max_length=250, verbose_name="Описание на слайде")
    image = models.ImageField(upload_to='slider_images/', verbose_name="Изображение слайда")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")

    class Meta:
        verbose_name = "Слайд парка"
        verbose_name_plural = "Слайды на главной"
        ordering = ['order', 'id']

    def __str__(self):
        return self.description[:50]


# НОВАЯ МОДЕЛЬ ДЛЯ НОВОСТЕЙ ПАРКА
class NewsArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок новости")
    summary = models.CharField(max_length=500, verbose_name="Краткое описание (для превью)")
    content = models.TextField(verbose_name="Полный текст новости")
    image = models.ImageField(upload_to='news_images/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']  # Свежие новости будут отображаться первыми

    def __str__(self):
        return self.title


# МОДЕЛЬ ДЛЯ МЕТОК ПОЛЬЗОВАТЕЛЕЙ НА ЯНДЕКС КАРТЕ
class UserMark(models.Model):
    CATEGORY_CHOICES = [
        ('idea', '💡 Предложение / Идея'),
        ('fix', '🛠 Благоустройство / Починить'),
        ('place', '🌲 Интересное место'),
    ]

    title = models.CharField(max_length=150, verbose_name="Заголовок / Имя")
    comment = models.TextField(verbose_name="Комментарий / Описание")
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='idea', 
        verbose_name="Категория"
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_approved = models.BooleanField(default=True, verbose_name="Одобрено (отображается на карте)")

    class Meta:
        verbose_name = "Метка на карте"
        verbose_name_plural = "Метки на карте"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_category_display()}: {self.title} [{self.latitude}, {self.longitude}]"