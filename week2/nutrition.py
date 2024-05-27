fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50
}



item = input("item: ").title().strip()


if item in fruits.keys():
    print(f"Calories: {fruits[item]}")






