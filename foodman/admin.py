from django.contrib import admin
from .models import Ingredients, Measures, Recipes, Compositions, Dishes, IngredientsStock, Meals, Meal2Dish


class FoodManAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


@admin.register(Ingredients)
class IngredientsAdmin(FoodManAdmin):
    fields = ('name', 'description', 'measure')
    list_display = ('name', 'description', 'measure')
    list_filter = ('name', 'measure')


@admin.register(Measures)
class MeasuresAdmin(FoodManAdmin):
    fields = ('name', 'description')
    list_display = ('name', 'description')
    list_filter = ('name',)


class CompositionsInline(admin.TabularInline):
    model = Compositions
    extra = 1


@admin.register(Recipes)
class RecipesAdmin(FoodManAdmin):
    inlines = [CompositionsInline]
    fields = ('name', 'description', 'persons')
    list_display = ('name', 'description', 'persons')
    list_filter = ('name', 'persons')


@admin.register(Dishes)
class DishesAdmin(FoodManAdmin):
    fields = ('name', 'description', 'persons')
    list_display = ('name', 'description', 'persons')
    list_filter = ('name', 'persons')


@admin.register(IngredientsStock)
class IngredientsStockAdmin(FoodManAdmin):
    fields = ('ingredient', 'amount')
    list_display = ('ingredient', 'amount')
    list_filter = ('ingredient',)


class Meal2DishInline(admin.TabularInline):
    model = Meal2Dish
    extra = 1


@admin.register(Meals)
class MealsAdmin(FoodManAdmin):
    inlines = [Meal2DishInline]
    fields = ('name', 'date')
    list_display = ('name', 'date')
    list_filter = ('name', 'date')
