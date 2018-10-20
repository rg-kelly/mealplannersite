from django.contrib import admin
from .models import Recipe, Ingredient, WeekOfDate, RecipeType, MealType, Day, Unit, CookbookType, Purchase, Store

# Register your models here.


class RecipeElementInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = [
        RecipeElementInLine,
    ]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeElementInLine,
               ]


class DayAssignmentInline(admin.TabularInline):
    model = WeekOfDate.recipes.through
    extra = 7


class WeekAdmin(admin.ModelAdmin):
    inlines = [
        DayAssignmentInline,
               ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(WeekOfDate, WeekAdmin)
admin.site.register(RecipeType)
admin.site.register(MealType)
admin.site.register(CookbookType)
admin.site.register(Day)
admin.site.register(Unit)
admin.site.register(Purchase)
admin.site.register(Store)
