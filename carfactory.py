from collections import Counter
from time import sleep


# Create a bank account to store money from car sales
class BankAccount:
    def __init__(self) -> None:
        self.balance: int = 0

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.balance += amount
            print(f'Deposited: ${amount}. New balance: ${self.balance}.')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew: ${amount}. New balance: ${self.balance}.')
        else:
            print('Insufficient funds or invalid withdrawal amount.')

    def get_balance(self) -> int:
        return self.balance
    

# 1. Create a car blueprint
class Car:
    def __init__(self, brand: str, color: str, model: int, sale_price: int) -> None:
        self.brand = brand
        self.color = color
        self.model = model
        self.sale_price = sale_price

    def drive(self, distance: int, speed: int) -> None:
        print(f'{self.brand} {self.model} [{self.color}] started journey...')
        for i in range(1, distance + 1):
            sleep(60 / speed)
            print(f'KM: {i}')

        print(f'{self.brand} {self.model} [{self.color}] completed journey...')


# 2. Test that the car works
def test_car() -> None:
    volvo: Car = Car('Volvo', 'Red', 200, 30000)
    volvo.drive(6, 140)


# 3. Create more cars
def create_cars(cars: list[Car]) -> None:
    # Everything is case-sensitive here
    brand: str = input('Enter the brand: ')
    color: str = input('Enter the color: ')
    try:
        model: int = int(input('Enter the model number: '))
        amount: int = int(input('Enter the no. of cars to create: '))
        car_price: int = int(input('Enter the sale price: '))

        for _ in range(amount):
            cars.append(Car(brand, color, model, car_price))

        print('Cars created!')
    except ValueError:
        print('Error, please enter model number, no. of cars to be created and price of the car as digits only.')


# 4. Display the stock
def display_stock(cars: list[Car]) -> None:
    car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model) for car in cars]
    counter: Counter[tuple[str, str, int]] = Counter(car_tuples)

    for (brand, model, color), count in counter.items():
        print(f'{brand} {model} [{color}]: {count} in stock')


# 5. Sell the cars
def sell_cars(cars: list[Car], bank_acct: BankAccount) -> None:
    # Everything is case-sensitive here
    brand: str = input('Enter the brand: ')
    color: str = input('Enter the color: ')
    try:
        model: int = int(input('Enter the model number: '))
        amount: int = int(input('Enter the number of cars to sell: '))

        car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model) for car in cars]
        counter: Counter[tuple[str, str, int]] = Counter(car_tuples)
        available: int = counter.total() #counter[(brand, color, model)]
        if available >= amount:
            sold: int = 0
            for i in range(len(cars) - 1, -1, -1):
                if cars[i].brand == brand and cars[i].color == color and cars[i].model == model:
                    bank_acct.deposit(cars[i].sale_price)
                    del cars[i]
                    sold += 1
                    if sold == amount:
                        print(f'Sold {amount} {brand} {model} [{color}] cars.')
                        print(f'Current bank balance: ${bank_acct.get_balance()}.')
                        break            
        else:
            print(f'Error, not enough cars in stock. Available in stock: {available}, requested to sell: {amount}.')
    except ValueError:
        print('Error, please enter numbers as digits only. E.g., "10" and not "ten".')


def main() -> None:
    cars: list[Car] = [Car('Volvo', 'Red', 200, 31000),
                       Car('Volvo', 'Red', 200, 31000),
                       Car('Toyota', 'Green', 321, 22000)]
    
    bank_acct: BankAccount = BankAccount()

    print('''Type: 
                  "create" to create cars.
                  "display" to display current stock.
                  "sell" to sell cars.
                  "exit" or "quit" to exit the program.''')
    
    while True:
        user_input: str = input('You: ').lower().strip()

        if user_input == 'create':
            create_cars(cars)
        elif user_input == 'display':
            display_stock(cars)
        elif user_input == 'sell':
            sell_cars(cars, bank_acct)
        elif user_input in ('exit', 'quit'):
            print('Exiting...')
            break
        else:
            print(f'Unknown command: "{user_input}"')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add a function that allows you to sell cars. It must be able to check stock
# and only sell if there's enough cars.
# 2. Create a bank to store the money you're making with your car sales.
# NAILED IT! AP Oct 14, 2025