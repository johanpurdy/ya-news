import pytest
from pytest_lazy_fixtures import lf
from pytest_django.asserts import assertRedirects

from django.urls import reverse
from http import HTTPStatus

from news.forms import CommentForm


@pytest.mark.django_db
def test_news_count(client, news):
    url = reverse('news:home')
    response = client.get(url)
    object_list = response.context['object_list']
    news_count = object_list.count()
    assert news_count <= 10


@pytest.mark.django_db
def test_news_ordering(client, news):
    url = reverse('news:home')
    response = client.get(url)
    object_list = response.context['object_list']
    all_dates = [news.date for news in object_list]
    sorted_dates = sorted(all_dates, reverse=True)
    assert all_dates == sorted_dates


@pytest.mark.django_db
def test_comments_ordering(client, news):
    url = reverse('news:detail', args=(news.pk,))
    response = client.get(url)
    news = response.context['news']
    comments = news.comment_set.all()
    all_timecreated_comment = [comment.created for comment in comments]
    sorted_timecreated = sorted(all_timecreated_comment)
    assert sorted_timecreated == all_timecreated_comment


def test_pages_contains_form(author_client, news):
    url = reverse('news:detail', kwargs={'pk': news.pk})
    response = author_client.get(url)
    assert 'form' in response.context
    assert isinstance(response.context['form'], CommentForm)