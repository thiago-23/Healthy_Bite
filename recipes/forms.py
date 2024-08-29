from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'instructions', 
            'ingredients',
            'cook_time', 
            'image',
            'status'
        ]