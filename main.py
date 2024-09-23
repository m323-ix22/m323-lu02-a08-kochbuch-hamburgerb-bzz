"""     Aufgabe: Kochbuch       """

import json


def load_recipe(recipe_json):
    return json.loads(recipe_json)


def adjust_recipe(original_recipe, num_people):
    for ingredient in original_recipe["ingredients"]:
        original_recipe["ingredients"][ingredient] = original_recipe["ingredients"][ingredient] / original_recipe[
            "servings"] * num_people
    original_recipe["servings"] = num_people
    return original_recipe


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe = ('{"title": "Spaghetti Bolognese", "ingredients": '
              '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    # Dein Code kommt hier hin
    adjusted_recipe = adjust_recipe(recipe, 2)
    loaded_recipe = load_recipe(recipe)
