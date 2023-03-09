from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeListViewTestCase(TestCase):

    def setUp(self):
        self.chef1 = User.objects.create_user(
            username='chef1',
            password='passwordchef1'
        )
        self.chef2 = User.objects.create_user(
            username='chef2',
            password='passwordchef2'
        )
        self.recipe1 = Recipe.objects.create(
            title='Recipe 1',
            ingredients='Ingredients 1',
            preparation_method='Preparation Method 1',
            chef=self.chef1
        )
        self.recipe2 = Recipe.objects.create(
            title='Recipe 2',
            ingredients='Ingredients 2',
            preparation_method='Preparation Method 2',
            chef=self.chef2
        )
        self.serializer1 = RecipeSerializer(instance=self.recipe1)
        self.serializer2 = RecipeSerializer(instance=self.recipe2)

    def test_get_all_recipes(self):
        """ This test check get all recipes """
        response = self.client.get(reverse('recipes:recipe-list'))
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_filtered_recipes_by_chef(self):
        """ This test check get filtered recipes by chef id """
        chef_filter = {'chef__id': 1}
        response = self.client.get(reverse('recipes:recipe-list'), chef_filter)
        recipes = Recipe.objects.filter(chef=self.chef1.id)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_filtered_recipes_by_search(self):
        """ This test check search recipe by title """
        search_filter = {'search': 'Recipe 2'}
        response = self.client.get(reverse('recipes:recipe-list'), search_filter)
        recipes = Recipe.objects.filter(title='Recipe 2')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
