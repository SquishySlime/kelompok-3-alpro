total_harga = 0

print(
    """
    1. Frankfurter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """
)
topping_pizza = int(input("Pilih Topping Pizza: "))
if topping_pizza == 1:
    topping_pizza = "Frankfurter BBQ"
elif topping_pizza == 2:
    topping_pizza = "Meat Monsta"
elif topping_pizza == 3:
    topping_pizza = "Super Supreme"
elif topping_pizza == 4:
    topping_pizza = "Super Supreme Chicken"

print(
    """
    1. Pan
    2. StuffedCrust Cheese
    3. StuffedCrust Sausage
    4. Cheesy Bites
    5. Crown Crust
    """
)
crust_pizza = int(input("Pilih Crust/Tepian Pizza: "))
if crust_pizza == 1:
    crust_pizza = "Pan"
    total_harga = 43_637
elif crust_pizza == 2:
    crust_pizza = "StuffedCrust Cheese"
    total_harga = 55_455
elif crust_pizza == 3:
    crust_pizza = "StuffedCrust Sausage"
    total_harga = 52_728
elif crust_pizza == 4:
    crust_pizza = "Cheesy Bites"
    total_harga = 57_273
elif crust_pizza == 5:
    crust_pizza = "Crown Crust"
    total_harga = 55_455

extra_cheese = input("Pakai Tambahan Keju (y/n): ").lower()
while extra_cheese not in ["y", "n"]:
    extra_cheese = input("Pakai Tambahan Keju (y/n): ").lower()
if extra_cheese == "y":
    total_harga += 13_636
    extra_cheese = True
elif extra_cheese == "n":
    extra_cheese = False

print("\nTerima Kasih telah membeli Pizza di Pizza Hut")
print(f"Pesanan Anda Pizza dengan Topping {topping_pizza}")
print(f"Crust/Pinggiran {crust_pizza} dan")
print(f"{'dengan' if extra_cheese else 'tanpa'} Tambahan Keju")
print(f"Total Harga: Rp {total_harga}")
