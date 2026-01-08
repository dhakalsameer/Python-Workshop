def shopping_list(**items):
    print("🛒 Shopping List")
    print("-" * 20)
    for item, quantity in items.items():
          print(f"{item:<15}: {quantity}")


shop = shopping_list(rice=2, milk=1, apples=6, bread=1)
print(shop)