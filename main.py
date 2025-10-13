print("Hello, Python!")
print("Running this program with keyboard shortcut of Ctrl+Alt+4")

# # Python does not have a "true" constant!
# # But by convention, we use ALL_CAPS for variables that should not change
# PI = 3.14159
# print(PI)
# #PI = 4  # This would be a bad idea BUT Python will not stop you
# #print(PI)

# # Constants
# MILES_TO_KM = 1.60934
# KM_TO_MILES = 0.621371

# # User input
# miles1 = float(input("Enter miles: "))
# km1 = miles1 * MILES_TO_KM

# km2 = float(input("Enter kilometers: "))
# miles2 = km2 * KM_TO_MILES

# # Display results
# print(f"{miles1} miles is {km1:.3f} kilometers")
# print(f"{km2} kilometers is {miles2:.3f} miles")

# USE Type hints !!(also called Type annotations)
# examples follow
# bank_balance: int = 500
# rate_of_interest: float = 5.35
# accrued_interest: float = bank_balance * (rate_of_interest / 100)
# new_balance: float = bank_balance + accrued_interest

# print(f"Original balance was ${bank_balance:.2f}")
# print(f"New balance is ${new_balance:.2f}")

# QUIZ QUESTIONS

# print(10 + '20') -- this will cause an error "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

# x: int = 'Hello Bob!'
# print(x) 
# This will run just fine and print Hello Bob! to the console!!!
# But if you use a type checker like mypy, it will flag this as an error
# Type hints are not enforced at runtime by Python itself
# They are mainly for static analysis tools and for better code readability

# numbers: list[int] = [1, 2, 3, 4, 5]
# names: list[str] = ["Alice", "Bob", "Charlie"]
# # without type hints, we can indeed set up a list!
# mixed_list = [1, "two", 3, True]  # This is valid in Python
# print(mixed_list)
# # But with type hints, we can specify the expected types
# # CORRECT way to write the above would be:
# mixed_list2: list[int | str | bool] = [1, "two", 3, True]
# print(mixed_list2)

# import formatter
# from faker import Faker

# print('Version: ', formatter.VERSION)
# user_input: str = input("Enter a title: ")
# print(f'Title: {formatter.format_title(user_input)}')

# fake = Faker()
# print("Fake name:", fake.name())
# print("Fake email:", fake.email())
