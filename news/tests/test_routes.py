from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from news.models import News


# class TestRoutes(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.news = News.objects.create(title='Заголовок', text='Текст')

#     def test_pages_availability(self):
#         urls = (
#             ('news:home', None),
#             ('news:detail', (self.news.id,)),
#             ('users:login', None),
#             ('users:logout', None),
#             ('users:signup', None),
#         )
#         for name, args in urls:
#             with self.subTest(name=name):
#                 url = reverse(name, args=args)
#                 response = self.client.get(url)
#                 self.assertEqual(response.status_code, HTTPStatus.OK)


# def test_availability_for_comment_edit_and_delete(self):
#     users_statuses = (
#         (self.author, HTTPStatus.OK),
#         (self.reader, HTTPStatus.NOT_FOUND),
#     )
#     for user, status in users_statuses:
#         self.client.force_login(user)
#         for name in ('news:edit', 'news:delete'):
#             with self.subTest(user=user, name=name):        
#                 url = reverse(name, args=(self.comment.id,))
#                 response = self.client.get(url)
#                 self.assertEqual(response.status_code, status)


# def test_redirect_for_anonymous_client(self):
#     # Сохраняем адрес страницы логина:
#     login_url = reverse('users:login')
#     # В цикле перебираем имена страниц, с которых ожидаем редирект:
#     for name in ('news:edit', 'news:delete'):
#         with self.subTest(name=name):
#             # Получаем адрес страницы редактирования или удаления комментария:
#             url = reverse(name, args=(self.comment.id,))
#             # Получаем ожидаемый адрес страницы логина, 
#             # на который будет перенаправлен пользователь.
#             # Учитываем, что в адресе будет параметр next, в котором передаётся
#             # адрес страницы, с которой пользователь был переадресован.
#             redirect_url = f'{login_url}?next={url}'
#             response = self.client.get(url)
#             # Проверяем, что редирект приведёт именно на указанную ссылку.
#             self.assertRedirects(response, redirect_url)