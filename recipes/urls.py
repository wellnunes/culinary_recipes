from django.urls import path
from recipes.views import RecipeList, RecipeDetail

app_name = 'recipes'

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]
