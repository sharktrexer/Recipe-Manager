from django import forms
from .models import Recipe, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__' # A security concern but this is ok for this app