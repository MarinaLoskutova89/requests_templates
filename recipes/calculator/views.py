from django.shortcuts import render

DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'butter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
        # можете добавить свои рецепты ;)
}

def home_view(request, recipes):
    mult_recipe = {}
    serving = request.GET.get('serving', 1)

    if recipes in DATA:
        recipe = DATA.get(recipes)
        for ingredient, amount in recipe.items():
            mult_amount = amount * int(serving)
            mult_recipe[ingredient] = mult_amount

        context = {
            'recipe': mult_recipe
        }
    else:
        context = {
            'recipe': None
        }
    return render(request, 'calculator/index.html', context)


