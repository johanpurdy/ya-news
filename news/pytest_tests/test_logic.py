import pytest

from http import HTTPStatus
from pytest_lazy_fixtures import lf
from http import HTTPStatus

from pytest_django.asserts import assertRedirects, assertFormError

from django.urls import reverse
from news.models import Comment, News
from news.forms import BAD_WORDS, WARNING


def test_user_create_comment(
    author_client,
    author,
    new_comment_form,
    news
):
    url = reverse('news:detail', kwargs={'pk': news.id})
    response = author_client.post(url, data=new_comment_form)
    assertRedirects(
        response,
        reverse('news:detail', kwargs={'pk': news.id}) + '#comments'
    )
    assert news.comment_set.count() == 1
    comment = Comment.objects.first()
    assert comment.text == new_comment_form['text']
    assert comment.news == news
    assert comment.author == author


def test_user_cant_use_bad_words(not_author_client, news):
    bad_words_data = {'text': f'Какой-то текст, {BAD_WORDS[0]}, еще текст'}
    url = reverse('news:detail', kwargs={'pk': news.id})
    # Отправляем запрос через авторизованный клиент.
    response = not_author_client.post(url, data=bad_words_data)
    form = response.context['form']
    assertFormError(
        form=form,
        field='text',
        errors=WARNING
    )
    comments_count = Comment.objects.count()
    assert comments_count == 0


def test_author_can_edit_comment(
        author_client,
        news,
        new_comment_form,
        comment
):
    url = reverse('news:edit', kwargs={'pk': news.id})
    author_client.post(url, new_comment_form)
    comment.refresh_from_db()
    assert comment.text == new_comment_form['text']


def test_not_author_cant_edit_comment(
        not_author_client,
        news,
        new_comment_form,
        comment
):
    url = reverse('news:edit', kwargs={'pk': news.id})
    response = not_author_client.post(url, new_comment_form)
    assert response.status_code == HTTPStatus.NOT_FOUND
    comment.refresh_from_db()
    assert comment.text != new_comment_form['text']
