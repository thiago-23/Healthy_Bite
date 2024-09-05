from django.urls import path
from .views import (
    Home,
    RecipeList,
    RecipeDetail,
    RecipeCreate,
    RecipeEdit,
    RecipeDelete,
    MyBookmarks,
    like_recipe,
    toggle_bookmark,
    MyRecipes,
    CommentUpdateView,
    CommentDeleteView 
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('recipe_display/', RecipeList.as_view(), name='recipe_display'),
    path('recipe-create/', RecipeCreate.as_view(), name='recipe_create'),
    path('recipe-edit/<slug:slug>/', RecipeEdit.as_view(), name='recipe_edit'),
    path('recipe-delete/<slug:slug>/', RecipeDelete.as_view(), name='recipe_delete'),
    path('mybookmarks/', MyBookmarks.as_view(), name='my_bookmarks'),
    path('recipe/<int:id>/like/', like_recipe, name='recipe_like'),
    path('recipe/<slug:slug>/bookmark/', toggle_bookmark, name='bookmark_recipe'),
    path('my-recipes/', MyRecipes.as_view(), name='my_recipes'),
    path('comment-update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment-delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe_detail'),
]
