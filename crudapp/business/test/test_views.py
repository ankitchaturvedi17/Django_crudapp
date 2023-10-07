from django import urls
from django.contrib.auth import get_user_model
import pytest

@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('create'),
    ('show')])
def test_render_views(client,param):
    temp = urls.reverse(param)
    resp = client.get(temp)
    assert resp.status_code ==200