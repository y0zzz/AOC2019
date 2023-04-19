# day_01_part_01.py
def fuel_required(mass):
    return mass // 3 - 2

if __name__ == '__main__':
    with open("input_day1") as file:
        data = file.read()
        data = data.splitlines()
        data_list = list(map(int, data))
