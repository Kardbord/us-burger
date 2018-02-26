from django.contrib import admin
from app.models import Recipe, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)