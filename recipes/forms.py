from django import forms
from .models import Recipe, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'headline',
            'description',
            'author',
        )

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'tags',
            'category',
            'description',
            'ingredients',
            'instructions',
            'notes',
            'prep_time',
            'cook_time',
            'image_source',
        )
