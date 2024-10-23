from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="A short description of the recipe")
    ingredients = models.TextField(help_text="List of ingredients by quantity")
    instructions = models.TextField(help_text="Step-by-step instructions to prepare the recipe")
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    total_time = models.IntegerField(help_text="Total time in minutes", blank=True)
    category = models.CharField(max_length=255, help_text="e.g. Breakfast, Lunch, Dinner, ...")
    image_source = models.CharField(max_length=255, help_text="Link to the image source of the recipe", blank=True)
    tags = models.TextField(help_text="How to describe the recipe, e.g. vegan, gluten-free, ...")
    notes = models.TextField(help_text="Additional notes about the recipe", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate the total time before saving
        # By overwriting the save() method
        self.total_time = self.prep_time + self.cook_time
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
