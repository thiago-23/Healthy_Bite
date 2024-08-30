from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe-create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe-edit/<slug:slug>/', views.RecipeEdit.as_view(), name='recipe_edit'),
    path('recipe-delete/<slug:slug>/', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('<slug:slug>/toggle_favourite/', views.toggle_favourite, name='toggle_favourite'),
]