"""Challenge 1.
--- Day 1: The Tyranny of the Rocket Equation ---
Challenge is here: https://adventofcode.com/2019/day/1
"""
from Challenges import utilities as util


def day_1(mass_list: list) -> int:
    """Get sum fuel required.
    mass: mass list
    """
    sum_fuel = 0
    for mass in mass_list:
        mass = int(mass)
        fuel_required = (mass // 3) - 2
        sum_fuel = sum_fuel + fuel_required
    return sum_fuel


if __name__ == "__main__":
    """Main function."""
    # Reading input file
    file_contents = util.read_txt_file("challenge_day1_input.txt")

    print(
        f"{day_1(file_contents)} That is the right answer! You are one gold star closer to rescuing Santa."
    )
