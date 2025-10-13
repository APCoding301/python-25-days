import json


# 1. Load the data
def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)


# 2. Create instructions
def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')


def convert(user_input: str, rates: dict[str, float]) -> dict[str, float]:
    # Prepare data
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]  # Gets the last three characters of a string
    final_dict: dict[str, float] = {}

    # Check whether the user specifies a valid currency
    if input_currency_code not in currency_codes:
        print(f'Currency code: "{input_currency_code}" is invalid.')
        return final_dict

    # Check whether the specifies a valid amount
    try:
        input_amount: float = float(user_input[:-3])  # Gets everything besides the last three characters
    except ValueError:
        print(f'"{user_input}" is invalid. Try something like: "10 AUD"')
        return final_dict

    # Base conversion - USD is the base currency in the file so any currency we specify
    # will be converted to that first.
    base_conversion: float = input_amount / rates[input_currency_code]

    # Prepare the final dictionary. First entry is the original amount and currency entered by the user.
    final_dict[input_currency_code] = round(input_amount, 2)

    for currency_code in currency_codes:
        converted_amount: float = base_conversion * rates[currency_code]
        final_dict[currency_code] = round(converted_amount, 2)

    return final_dict


def print_converted_currencies(final_dict: dict[str, float]) -> None:
    print(f'{list(final_dict.values())[0]:>16} {list(final_dict.keys())[0]}')  # >16 means right align with 16 spaces
    print('-' * 20)
    for code, amount in final_dict.items():
        print(f'= {amount:>14} {code}')  # right align with 14 spaces
    print('-' * 20)


def main() -> None:
    # 1. Display instructions
    instructions()

    # 2. Load exchange rate data
    exchange_rates: dict[str, float] = load_exchange_rates()

    # 3. Run
    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {", ".join(exchange_rates.keys())}')
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        final_dict_print: dict[str, float] = convert(user_input, exchange_rates)

        if final_dict_print:
            print_converted_currencies(final_dict_print)
        else:
            print('No conversions to display. Try again. Type "10 AUD" to convert 10 AUD to various currencies. Type LIST to see available currencies.')


if __name__ == '__main__':
    main()

# Homework:
# NAILED IT !! AP -- Oct 13, 2025
# 1. Split "convert()" into two functions:
# - One that returns all the conversions as a dictionary.
# - One that displays the converted data.