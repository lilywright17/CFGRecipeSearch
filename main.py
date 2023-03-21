import requests

def recipe_search(ingredient, health_restriction, meal_type):
    app_id = '3b7cc3df'
    app_key = 'f1ad8a8ef4ed830b8ff5c1877f327ea1'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&Health={}&mealType={}'.format(ingredient, app_id, app_key, health_restriction, meal_type))
    data = result.json()
    return data['hits']

def run():
    ingredient = input("Enter an ingredient you'd like to use: ")
    meal_type = input("Choose which meal type you would like: \n breakfast \n lunch \n dinner \n snack \n >")
    health_restriction = input("Please select a dietary requirement: \n vegan \n vegetarian \n gluten-free \n None \n >")
    max_no_of_calories = int(input('Enter the maximum amount of calories you would like: '))

    results = recipe_search(ingredient, health_restriction, meal_type)
    for result in results:
        recipe = result['recipe']
        if recipe["calories"] < max_no_of_calories:
            print(recipe["label"])
            print(recipe["calories"])
            print(recipe["uri"])
            print(recipe["mealType"])
            print(recipe["cuisineType"])
            print()

run()
