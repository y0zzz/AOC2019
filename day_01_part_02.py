# day_01_part_02.py
def fuel_required(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_required(fuel)
