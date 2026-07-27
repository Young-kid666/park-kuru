import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Feedback, ParkSlide, NewsArticle, UserMark 

# ==========================================
# ВСТРОЕННАЯ ФУНКЦИЯ ОТПРАВКИ В TELEGRAM
# ==========================================
TELEGRAM_BOT_TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER'
TELEGRAM_CHAT_ID = 'ТВОЙ_CHAT_ID'

def send_telegram_message(text):
    """Функция отправки сообщений в Telegram"""
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER':
        return  # Если токен не настроен, просто пропускаем
        
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")


def home(request):
    slides = ParkSlide.objects.filter(is_active=True)
    news = NewsArticle.objects.filter(is_published=True).order_by('-created_at')[:3]
    return render(request, 'kura_park/index.html', {'slides': slides, 'news': news})


def news_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk, is_published=True)
    return render(request, 'kura_park/news_detail.html', {'article': article})


def about(request):
    return render(request, 'kura_park/about.html')


def museum(request):
    return render(request, 'kura_park/museum.html')


def thermal(request):
    return render(request, 'kura_park/thermal.html')


def temple(request):
    return render(request, 'kura_park/temple.html')


def contacts(request):
    success_flag = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        agreement = request.POST.get('agreement')
        
        if agreement:
            Feedback.objects.create(
                name=name, 
                email=email, 
                message=message_text
            )
            
            tg_text = (
                f"📩 <b>Новое обращение на сайте!</b>\n\n"
                f"<b>От кого:</b> {name}\n"
                f"<b>Email:</b> {email}\n"
                f"<b>Сообщение:</b>\n{message_text}"
            )
            send_telegram_message(tg_text)

            success_flag = True
            return render(request, 'kura_park/contacts.html', {'success': success_flag})
        
    return render(request, 'kura_park/contacts.html', {'success': success_flag})


# ==========================================
# РАБОТА С ИНТЕРАКТИВНОЙ КАРТОЙ
# ==========================================

def map_view(request):
    return render(request, 'kura_park/map.html')


def get_marks(request):
    marks = UserMark.objects.filter(is_approved=True).values('title', 'comment', 'category', 'latitude', 'longitude')
    return JsonResponse(list(marks), safe=False)


def add_mark(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title', 'Без названия')
            comment = data.get('comment', '')
            category = data.get('category', 'idea')
            lat = data.get('lat')
            lng = data.get('lng')

            UserMark.objects.create(
                title=title,
                comment=comment,
                category=category,
                latitude=lat,
                longitude=lng
            )

            cat_names = {
                'idea': '💡 Предложение / Идея',
                'fix': '🛠 Благоустройство / Починить',
                'place': '🌲 Интересное место'
            }
            cat_label = cat_names.get(category, 'Метка')

            tg_text = (
                f"📍 <b>Новая метка на карте!</b>\n\n"
                f"<b>Категория:</b> {cat_label}\n"
                f"<b>Заголовок/Имя:</b> {title}\n"
                f"<b>Комментарий:</b> {comment}\n\n"
                f"🗺 <a href='https://yandex.ru/maps/?pt={lng},{lat}&z=17&l=map'>Посмотреть на Яндекс Картах</a>"
            )
            send_telegram_message(tg_text)

            return JsonResponse({'status': 'ok', 'message': 'Метка успешно добавлена!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Недопустимый метод'}, status=405)