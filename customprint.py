from typing import Any

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# 1. Hover over print to see the original signature
def custom_print(*values: Any,
                 sep: str | None = " ",
                 end: str | None = "\n",
                 caps: bool = False,
                 count: bool = False,
                 colorText: bool = False,
                 include_types: bool = False) -> None:

    new_values: list[Any] = []
    # Counts the number of elements being printed if flag is toggled
    if count:
        if colorText:
            new_values.append(f'{Colors.RED}{Colors.UNDERLINE}Number of elements: {len(values)}{Colors.RESET}')
        else:
            new_values.append(f'Number of elements: {len(values)}')

    # Uppercases all string values if flag is toggled
    for value in values:
        if isinstance(value, str) and caps:
            new_values.append(value.upper())
        else:
            new_values.append(value)

    # Includes type of every argument if flag is toggled
    values_with_type: list[Any] = []
    if include_types:
        for value in new_values:
            values_with_type.append((value, type(value)))

        print(*values_with_type, sep=sep, end=end)
    else:
        print(*new_values, sep=sep, end=end)


# 2. Have fun with custom printing!
custom_print('Bob', 'James', 10, count=True, caps=False, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, count=True, caps=True, include_types=False, sep=', ', end='!\n')
custom_print('Bob', 'James', 10, count=True, include_types=True, sep=', ', end='!\n')
custom_print([], count=True, include_types=True, sep=', ', end='!\n')
custom_print('Bob', 'James', 10, colorText=True, count=True, caps=False, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, count=True, caps=False, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, colorText=True, count=True, caps=True, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, 'Sally', 20, 30, 40, colorText=True, count=True, caps=False, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, 'Sally', 20, 30, 40, colorText=False, count=True, caps=True, include_types=True, sep=', ', end='!\n')
custom_print('Bob', 'James', 10, 'Sally', 20, 30, 40, colorText=True, count=True, caps=True, include_types=True, sep=', ')
# This above test case has a BUG! TOFIX: !! When all flags are True, doesn't print the first element in RED and UNDERLINE!


# Homework:
# 1. Add a field that counts the number of elements being printed.
# -- DONE! AP Oct 7, 2025
# 2. Add your very own feature to the custom print function.
# -- DONE! AP Oct 7, 2025
# -- a. I want to print the first element in 'red' color AND underlined in the terminal IF count=True :)
# -- b. colorText is the toggle for this feature.
# Below is what I found on how to print 'in color' using ANSI escape sequences:
# To print colored text in the Python console, you can use ANSI escape sequences or a dedicated library like termcolor or colorama.
# 1. Using ANSI Escape Sequences (Cross-platform, but more manual):
# ANSI escape sequences are special character sequences that terminals interpret to control text formatting, including color.
# class Colors:
#     RESET = '\033[0m'
#     RED = '\033[91m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     BLUE = '\033[94m'
#     MAGENTA = '\033[95m'
#     CYAN = '\033[96m'
#     WHITE = '\033[97m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#
# print(Colors.RED + "This text is red." + Colors.RESET)
# print(Colors.BOLD + Colors.GREEN + "This text is bold and green." + Colors.RESET)
# print(Colors.CYAN + Colors.UNDERLINE + "This text is cyan and underlined." + Colors.RESET)