# news/tests/test_content.py
from django.conf import settings
from django.test import TestCase
# Импортируем функцию reverse(), она понадобится для получения адреса страницы.
from django.urls import reverse

from news.models import News


class TestHomePage(TestCase):
    # Вынесем ссылку на домашнюю страницу в атрибуты класса.
    HOME_URL = reverse('news:home')

    @classmethod
    def setUpTestData(cls):
        all_news = [
            News(title=f'Новость {index}', text='Просто текст.')
            for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
        ]
        News.objects.bulk_create(all_news)

    # def test_news_count(self):
    #     # Загружаем главную страницу.
    #     response = self.client.get(self.HOME_URL)
    #     # Код ответа не проверяем, его уже проверили в тестах маршрутов.
    #     # Получаем список объектов из словаря контекста.
    #     object_list = response.context['object_list']
    #     # Определяем количество записей в списке.
    #     news_count = object_list.count()
    #     # Проверяем, что на странице именно 10 новостей.
    #     self.assertEqual(news_count, settings.NEWS_COUNT_ON_HOME_PAGE)

    # def test_news_order(self):
    #     response = self.client.get(self.HOME_URL)
    #     object_list = response.context['object_list']
    #     # Получаем даты новостей в том порядке, как они выведены на странице.
    #     all_dates = [news.date for news in object_list]
    #     # Сортируем полученный список по убыванию.
    #     sorted_dates = sorted(all_dates, reverse=True)
    #     # Проверяем, что исходный список был отсортирован правильно.
    #     self.assertEqual(all_dates, sorted_dates)

    # def test_comments_order(self):
    #     response = self.client.get(self.detail_url)
    #     # Проверяем, что объект новости находится в словаре контекста
    #     # под ожидаемым именем - названием модели.
    #     self.assertIn('news', response.context)
    #     # Получаем объект новости.
    #     news = response.context['news']
    #     # Получаем все комментарии к новости.
    #     all_comments = news.comment_set.all()
    #     # Собираем временные метки всех комментариев.
    #     all_timestamps = [comment.created for comment in all_comments]
    #     # Сортируем временные метки, менять порядок сортировки не надо.
    #     sorted_timestamps = sorted(all_timestamps)
    #     # Проверяем, что временные метки отсортированы правильно.
    #     self.assertEqual(all_timestamps, sorted_timestamps)

    # def test_anonymous_client_has_no_form(self):
    #     response = self.client.get(self.detail_url)
    #     self.assertNotIn('form', response.context)
        
    # def test_authorized_client_has_form(self):
    #     # Авторизуем клиент при помощи ранее созданного пользователя.
    #     self.client.force_login(self.author)
    #     response = self.client.get(self.detail_url)
    #     self.assertIn('form', response.context)
    #     # Проверим, что объект формы соответствует нужному классу формы.
    #     self.assertIsInstance(response.context['form'], CommentForm)