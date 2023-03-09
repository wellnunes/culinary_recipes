from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe


class RecipeModelTestCase(TestCase):

    def setUp(self):
        self.chef = User(
            id=1
        )
        self.recipe = Recipe(
            title="Test Recipe",
            ingredients="Many Ingredients",
            preparation_method="Many things",
            chef=self.chef
        )

    def test_recipe_attributes(self):
        """ This test check recipe status default value (True) """
        self.assertEqual(self.recipe.title, "Test Recipe")
        self.assertEqual(self.recipe.ingredients, "Many Ingredients")
        self.assertEqual(self.recipe.preparation_method, "Many things")
        self.assertEqual(self.recipe.chef, self.chef)
        self.assertEqual(self.recipe.status, True)
