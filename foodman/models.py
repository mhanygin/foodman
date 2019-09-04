from django.db import models


class FoodManModel(models.Model):
    class Meta:
        abstract = True


class Measures(FoodManModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ingredients(FoodManModel):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    measure = models.ForeignKey(Measures, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Recipes(FoodManModel):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    persons = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Compositions(FoodManModel):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=1)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} ({} {})'.format(self.ingredient, self.amount, self.ingredient.measure)


class Dishes(FoodManModel):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    dish_persons = models.PositiveIntegerField(default=1)
    dish_recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class IngredientsStock(FoodManModel):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.PositiveIntegerField(default=1)


class Meals(FoodManModel):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return '{} ({})'.format(self.name, self.date)


class Meal2Dish(FoodManModel):
    dish = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.meal, self.dish)
