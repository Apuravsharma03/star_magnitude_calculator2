import math


def calculate_absolute_magnitude(apparent_magnitude, distance_parsecs):
    """
    Calculate the absolute magnitude of a star given its apparent magnitude and distance in parsecs.

    :param apparent_magnitude: The apparent magnitude of the star.
    :param distance_parsecs: The distance to the star in parsecs.
    :return: The absolute magnitude of the star.
    """
    try:
        absolute_magnitude = apparent_magnitude - 5 * (math.log10(distance_parsecs)) + 5
        return absolute_magnitude
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return None


def main():
    print("Star Magnitude Calculator")
    try:
        apparent_magnitude = float(input("Enter the apparent magnitude of the star: "))
        distance_parsecs = float(input("Enter the distance to the star in parsecs: "))

        if distance_parsecs <= 0:
            print("Distance must be greater than zero.")
            return

        absolute_magnitude = calculate_absolute_magnitude(apparent_magnitude, distance_parsecs)
        if absolute_magnitude is not None:
            print(f"The absolute magnitude of the star is: {absolute_magnitude:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()