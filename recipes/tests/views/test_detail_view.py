from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeDetailViewTestCase(TestCase):

    def setUp(self):
        self.chef = User.objects.create_user(
            username='chef',
            password='passwordchef'
        )
        self.recipe = Recipe.objects.create(
            title='Recipe 1',
            ingredients='Ingredients 1',
            preparation_method='Preparation Method 1',
            chef=self.chef
        )
        self.serializer = RecipeSerializer(instance=self.recipe)

    def test_valid_recipe_detail(self):
        """ This test check valid recipe detail  """
        response = self.client.get(reverse('recipes:recipe-detail', kwargs={'pk': self.recipe.pk}))
        recipe = Recipe.objects.get(pk=self.recipe.pk)
        serializer = RecipeSerializer(recipe)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_recipe_detail(self):
        """ This test check invalid recipe creation  """
        response = self.client.get(reverse('recipes:recipe-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
