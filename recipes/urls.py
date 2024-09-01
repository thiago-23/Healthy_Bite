from django.urls import path
from .views import (
    RecipeList, RecipeDetail, RecipeCreate, RecipeEdit, RecipeDelete,
    MyBookmarks, like_recipe, BookmarkRecipe 
)

urlpatterns = [
    path('', RecipeList.as_view(), name='home'),
    path('recipe-create/', RecipeCreate.as_view(), name='recipe_create'),
    path('recipe-edit/<slug:slug>/', RecipeEdit.as_view(), name='recipe_edit'),
    path('recipe-delete/<slug:slug>/', RecipeDelete.as_view(), name='recipe_delete'),
    path('mybookmarks/', MyBookmarks.as_view(), name='my_bookmarks'),
    path('recipe/<int:id>/like/', like_recipe, name='recipe_like'),
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/<slug:slug>/bookmark/', BookmarkRecipe.as_view(), name='bookmark_recipe'),
]

