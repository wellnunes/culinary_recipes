from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from recipes.models import Recipe


class RecipeCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.chef = User.objects.create_user(
            username='chef',
            password='passwordchef'
        )
        self.client.force_authenticate(user=self.chef)
        self.valid_payload = {
            'title': 'Recipe 1',
            'ingredients': 'Ingredients 1',
            'preparation_method': 'Preparation Method 1',
            'chef': self.chef.id,
        }
        self.invalid_payload = {
            'title': '',
            'ingredients': 'Ingredients 2',
            'preparation_method': 'Preparation Method 2',
            'chef': self.chef.id,
        }

    def test_valid_recipe_creation(self):
        """ This test check valid recipe creation  """
        response = self.client.post(
            reverse('recipes:recipe-create'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.get().title, 'Recipe 1')

    def test_invalid_recipe_creation(self):
        """ This test check invalid recipe creation """
        response = self.client.post(
            reverse('recipes:recipe-create'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
