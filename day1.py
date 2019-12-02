INPUT_FILENAME = "day1input.txt"


def main():
    total_mass = 0
    fuel_mass = 0
    with open(INPUT_FILENAME) as f:
        for line in f:
            total_mass += (int(line) // 3) - 2
            fuel_mass += calculate_fuel(int(line))
    print("part 1: " + str(total_mass))
    print("part 2: " + str(fuel_mass))


def calculate_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel < 0:
        return 0
    return fuel + calculate_fuel(fuel)


if __name__ == "__main__":
    main()
