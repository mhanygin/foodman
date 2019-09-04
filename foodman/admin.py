from django.contrib import admin
from .models import Ingredients, Measures, Recipes, Compositions, Dishes, IngredientsStock, Meals, Meal2Dish


class FoodManAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredients)
class IngredientsAdmin(FoodManAdmin):
    pass


@admin.register(Measures)
class MeasuresAdmin(FoodManAdmin):
    pass


class CompositionsInline(admin.TabularInline):
    model = Compositions
    extra = 1


@admin.register(Recipes)
class RecipesAdmin(FoodManAdmin):
    inlines = [CompositionsInline]


# @admin.register(Compositions)
# class CompositionsAdmin(FoodManAdmin):
#     pass


@admin.register(Dishes)
class DishesAdmin(FoodManAdmin):
    pass


@admin.register(IngredientsStock)
class IngredientsStockAdmin(FoodManAdmin):
    pass


class Meal2DishInline(admin.TabularInline):
    model = Meal2Dish
    extra = 1


@admin.register(Meals)
class MealsAdmin(FoodManAdmin):
    inlines = [Meal2DishInline]
