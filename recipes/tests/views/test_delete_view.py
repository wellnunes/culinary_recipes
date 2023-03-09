from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from recipes.models import Recipe


class RecipeDeleteTestCase(TestCase):

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

    def test_delete_valid_recipe(self):
        """ This test check valid deletion """
        response = self.client.delete(
            reverse('recipes:recipe-delete', kwargs={'pk': self.recipe.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_recipe(self):
        """ This test check invalid deletion """
        response = self.client.delete(
            reverse('recipes:recipe-delete', kwargs={'pk': 999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
