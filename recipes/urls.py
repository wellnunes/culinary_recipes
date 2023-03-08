from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from recipes.views import RecipeList, RecipeDetail

app_name = 'recipes'

schema_view = get_schema_view(
   openapi.Info(
      title="Culinary Recipes API",
      default_version='v1',
      description="Simple API to maintain culinary recipes. Enabling the registration, editing and deletion of these"
                  " by chefs, in addition to queries and filters by unauthenticated users.",
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
