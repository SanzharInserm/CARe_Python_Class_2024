import math


def calculate_growth_rate(initial_count, final_count, time):
    """
    Calculate the growth rate of a microbial culture.

    :param initial_count: Initial cell count
    :param final_count: Final cell count
    :param time: Time elapsed
    :return: Growth rate
    """
    return (math.log(final_count) - math.log(initial_count)) / time


def get_positive_float_input(prompt):
    """
    Get a positive float input from the user.

    :param prompt: The input prompt to display
    :return: A positive float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def main():
    print("Microbial Growth Rate Calculator")
    print("--------------------------------")

    try:
        initial_count = get_positive_float_input("Enter the initial cell count: ")
        final_count = get_positive_float_input("Enter the final cell count: ")
        time = get_positive_float_input("Enter the time elapsed (in hours): ")

        growth_rate = calculate_growth_rate(initial_count, final_count, time)

        print(f"\nThe growth rate is: {growth_rate:.4f} per hour")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
#YOUR CODE FOR EX_0 INTERMEDIATE HERE