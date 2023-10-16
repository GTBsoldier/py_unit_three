# Assignment Three
# 2023-10-16
# Overall Purpose: Calculate the surface area of a rectangular prism.

def area_of_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The computed area.
    """
    return length * width

def surface_area(length, width, height):
    """
    Calculate the total surface area of a rectangular prism.

    :param length: The length of the prism.
    :param width: The width of the prism.
    :param height: The height of the prism.
    :return: The total surface area.
    """
    # Calculate the areas of all six sides of the rectangular prism
    top_bottom = 2 * area_of_rectangle(length, width)
    front_back = 2 * area_of_rectangle(length, height)
    left_right = 2 * area_of_rectangle(width, height)

    return top_bottom + front_back + left_right

def print_instructions():
    """
    Print the purpose of the program and instructions for the user.
    """
    print("This program calculates the surface area of a rectangular prism.")
    print("Please enter the following dimensions:")

def get_length():
    """
    Ask the user for the length and return the value.

    :return: The length entered by the user.
    """
    return float(input("Enter the length: "))

def get_width():
    """
    Ask the user for the width and return the value.

    :return: The width entered by the user.
    """
    return float(input("Enter the width: "))

def get_height():
    """
    Ask the user for the height and return the value.

    :return: The height entered by the user.
    """
    return float(input("Enter the height: "))

def main():
    print_instructions()
    length = get_length()
    width = get_width()
    height = get_height()

    total_surface_area = surface_area(length, width, height)
    print(f"The total surface area of the rectangular prism is {total_surface_area} square units.")

if __name__ == "__main__":
    main()
