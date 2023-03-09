from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from recipes.models import Recipe


class RecipeUpdateViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.chef = User.objects.create_user(
            username='chef',
            password='passwordchef'
        )
        self.client.force_authenticate(user=self.chef)
        self.recipe = Recipe.objects.create(
            title='Recipe 1',
            ingredients='Ingredients 1',
            preparation_method='Preparation Method 1',
            chef=self.chef
        )
        self.valid_payload = {
            'title': 'Recipe 1',
            'ingredients': 'Ingredients 1',
            'preparation_method': 'Preparation Method 1',
            'chef': self.chef.id,
        }
        self.invalid_payload = {
            'title': '',
            'ingredients': '',
            'preparation_method': '',
            'chef': '',
        }

    def test_valid_update_recipe(self):
        """ This test check valid update """
        response = self.client.put(
            reverse('recipes:recipe-update', kwargs={'pk': self.recipe.id}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_recipe(self):
        """ This test check invalid update """
        response = self.client.put(
            reverse('recipes:recipe-update', kwargs={'pk': self.recipe.id}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
