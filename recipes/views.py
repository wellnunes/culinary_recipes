from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListAPIView):
    """ List View w/ public permissions to list all recipes and perform searches and filters using query parameters """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['chef__id']
    search_fields = ['title', 'ingredients', 'preparation_method']
    permission_classes = [permissions.AllowAny]


class RecipeDetail(generics.RetrieveAPIView):
    """ Detail View w/ public permissions """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class RecipeCreate(generics.CreateAPIView):
    """ Create View w/ permissions only for authenticated users (chef's) """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeUpdate(generics.UpdateAPIView):
    """ Update View w/ permissions only for authenticated users (chef's) """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipeDelete(generics.DestroyAPIView):
    """ Delete View w/ permissions only for authenticated users (chef's) """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
