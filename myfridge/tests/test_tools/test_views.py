import pytest
from django.urls import reverse
from tools.views import bmiView, ShoppingListCreateView, ShoppingListUpdateView, ShoppingListDeleteView, ShoppingListView
from test_data.models_fixtures import (
    authenticated_user,
    client_with_authenticated_user,
    bmi_form_data,
    shopping_list
)


def test_bmiView(client, bmi_form_data):
    response = client.post(reverse('tools:bmi'), bmi_form_data)
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmi_result' in response.context


def test_shopping_list_create_viewe_success_response_get_method(client_with_authenticated_user):
    response = client_with_authenticated_user.get(reverse('tools:shopping_list_create'))
    assert response.status_code == 200

def test_shopping_list_update_view_success_response_get_method(client_with_authenticated_user, shopping_list):
    response = client_with_authenticated_user.get(reverse('tools:shopping_list_update', kwargs={'pk': shopping_list.pk}))
    assert response.status_code == 200

def test_shopping_list_view_success_response_get_method(client_with_authenticated_user, shopping_list):
    response = client_with_authenticated_user.get(reverse('tools:shopping_list'))
    assert response.status_code == 200
    assert 'object_list' in response.context