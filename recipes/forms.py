from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class RecipeForm(forms.ModelForm):
    """ Create Recipe Form """
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={"placeholder": 'title'})

    class Meta:
        model = Recipe
        fields = ['title', 
        'ingredients', 
        'instructions', 
        'image', 
        'status', 
        'cook_time'
        ]

        widgets = {
            'instructions': SummernoteWidget(),
            'ingredients': SummernoteWidget()
        }