from django.db import models

# Represents a recipe
class Recipe(models.Model):
    title = models.CharField(max_length=100, help_text="The title of the recipe")
    tags = models.TextField(help_text="How to describe the recipe, e.g. vegan, gluten-free, ...")
    category = models.CharField(max_length=100, help_text="e.g. Breakfast, Lunch, Dinner, ...")
    description = models.TextField(help_text="A short description of the recipe")
    ingredients = models.TextField(help_text="List of ingredients and their quantity")
    instructions = models.TextField(help_text="Step-by-step instructions to prepare the recipe")
    notes = models.TextField(help_text="Additional notes about the recipe", blank=True)
    
    prep_time = models.IntegerField(help_text="Preparation time in minutes")
    cook_time = models.IntegerField(help_text="Cooking time in minutes")
    total_time = models.IntegerField(help_text="Total time in minutes", blank=True)
    
    image_source = models.TextField( help_text="Link to the image source of the recipe", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate the total time before saving
        # By overwriting the save() method
        self.total_time = self.prep_time + self.cook_time
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Represents a review
class Review(models.Model):
    headline = models.CharField(
        label='Headline',
        max_length=50,
        help_text='Great recipe!',
    )
    description = models.CharField(
        label='Your Comments',
        widget=models.Textarea,
        help_text='My family didn\'t leave any leftovers!',
    )
    author = models.CharField(
        label='Author',
        max_length=100,
        help_text='Johnny McGee',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #TODO: perhaps add a rating field?
    
    def __str__(self):
        return self.headline
