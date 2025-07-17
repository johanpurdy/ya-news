import pytest
from pytest_lazy_fixtures import lf
from pytest_django.asserts import assertRedirects

from django.urls import reverse
from http import HTTPStatus

@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, args',
    (
        ('news:home', None),
        ('news:detail', 'id'),
        ('users:login', None),
        ('users:signup', None),
    )
)
def test_pages_availability(client, name, news, args):
    if args == 'id':
        url = reverse(name, args=(news.id,))
    else:
        url = reverse(name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (lf('not_author_client'), HTTPStatus.NOT_FOUND),
        (lf('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'name',
    (
        ('news:delete'),
        ('news:edit'),
    )
)
def test_availability_for_comment_edit_and_delete(
    name,
    comment,
    parametrized_client,
    expected_status,
):
    url = reverse(name, args=(comment.pk,))
    response = parametrized_client.get(url)
    assert response.status_code == expected_status


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    ('news:edit', 'news:delete')
)
def test_redirect_for_anonymous_client(client, comment, name):
    login_url = reverse('users:login')
    url = reverse(name, args=(comment.id,))
    redirect_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, redirect_url)
