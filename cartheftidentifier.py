# 1. Create the concept of a car in this world
class Car:
    def __init__(self, licence_plate: str) -> None:
        if len(licence_plate) != 6:
            raise ValueError('Invalid licence plate.')

        self.licence_plate = licence_plate


# 2. Create a place to store stolen cars
class StolenCarRegistry:
    def __init__(self) -> None:
        # Example: Set of license plates that are stolen
        self.stolen_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def is_stolen(self, plate: str) -> bool:
        return plate.upper() in self.stolen_plates


def display_options() -> None:
    print('Options:')
    print('0 - Display main menu options')
    print('1 - Check stolen car')
    print('2 - Remove stolen car(s)')
    print('3 - Count stolen cars')
    print('4 - Display all stolen plates')
    print('_')


def get_option(option: str) -> int:
    try:
        converted: int = int(option)
    except ValueError:
        print(f'Error, please enter a valid option.')
        return 0

    if converted == 0:
        return 0
    elif converted == 1:
        return 1
    elif converted == 2:
        return 2
    elif converted == 3:
        return 3
    elif converted == 4:
        return 4
    else:
        return 0
    

def remove_stolen_cars(registry: StolenCarRegistry) -> None:
    plate: str = input('Enter car licence plate to remove: ').strip().upper()   
    car: Car = Car(plate)
    try:
        if registry.is_stolen(car.licence_plate):
            registry.stolen_plates.remove(car.licence_plate)
            print(f'✅ Car with plate "{car.licence_plate}" has been removed from stolen registry.')
        else:
            print(f'❌ Car with plate "{car.licence_plate}" is not in the stolen registry.')
    except KeyError:
        print(f'❌ Car with plate "{car.licence_plate}" could not be found in the stolen registry.')
        

def check_stolen_car(registry: StolenCarRegistry) -> None:

    plate: str = input('Enter car licence plate: ').strip()
    car: Car = Car(plate)
    if registry.is_stolen(car.licence_plate):
        print(f'❌ Car with plate "{car.licence_plate}" is: REPORTED STOLEN!')
    else:
        print(f'✅ Car with plate "{car.licence_plate}" is: OK')


# 3. Check for stolen cars, remove stolen cars, count stolen cars and display all stolen plates
def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()
    # # Populate with some stolen plates
    registry.add_stolen_plates(['ABC123', 'XYZ999', 'BOB789'])

    print('Welcome to Car Theft Identifier')

    display_options()
    while True:
        user_input: str = input('You: ')
        menu_option: int = get_option(user_input)
        if menu_option == 0:
            display_options()
        elif menu_option == 1:
            check_stolen_car(registry)
        elif menu_option == 2:
            remove_stolen_cars(registry)
        elif menu_option == 3:
            print(f'Total stolen cars: {len(registry.stolen_plates)}')
        elif menu_option == 4:
            if registry.stolen_plates:
                print('Stolen Plates:')
                for plate in registry.stolen_plates:
                    print(plate)
            else:
                print('No stolen plates recorded.')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add a way to remove stolen cars from the StolenCarRegistry.
# 2. Add functionality that counts the total amount of stolen cars.
# 3. Add functionality that displays all the stolen plates.