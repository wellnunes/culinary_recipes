from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeSerializerTestCase(TestCase):

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
        self.serializer = RecipeSerializer(instance=self.recipe)

    def test_serialized_fields(self):
        """ This test check recipe serialized fields """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "title", "ingredients", "preparation_method", "chef", "status"})
