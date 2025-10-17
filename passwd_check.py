import string


# 1. Create the blueprint
class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] = self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r') as file:
            return {line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    def rate(self, password: str) -> tuple[str, int]:
    # This method returns a tuple of (rating, score)
    # rating is a string, score is an integer
    # rating can be 'secure', 'medium', 'poor', 'very poor', or 'DANGER! HIGH RISK!!'
    # score is 3 for secure, 2 for medium, 1 for poor, 0 for very poor, -1 for DANGER! HIGH RISK!!

        if self.is_common(password):
            return 'DANGER! HIGH RISK!!', -1

        # Calculate score
        score: int = 0
        # if any(c.isupper() for c in password) or any(c.isdigit() for c in password):  # Checks for uppercase characters OR numbers
        #     score += 1
        # if any(c in string.punctuation for c in password):  # Checks for punctuation
        #     score += 1
        # if len(password) >= 10:  # Checks length
        #     score += 1
        if len(password) >= 10:  # Checks length
            score += 1
        if any(c.isupper() for c in password):  # Checks for uppercase characters
            score += 1
        if any(c.isdigit() for c in password): # Checks for numbers
            score += 1
        if any(c in string.punctuation for c in password):  # Checks for punctuation
            score += 1

        # Return rating and score
        if score == 4:
            return 'very secure', 4
        elif score == 3:
            return 'secure', 3
        elif score == 2:
            return 'medium', 2
        elif score == 1:
            return 'poor', 1
        elif score == 0:
            return 'very poor', 0
        else:
            return 'DANGER! HIGH RISK!!', -1


# 2. Check for password
def main() -> None:
    # Link: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        rating, score = validator.rate(password)
        if rating == 'secure' and score == 3:
            print('✅ Your password is secure! Your passwd has 10 or more characters, it has symbols/punctuation,numbers and lowercase as well as uppercase letters.')
        elif rating == 'medium' and score == 2:
            print('⚠️ Your password is of medium strength. It does have 10 characters or more AND a mix of lowercase and uppercase letters.')
        elif rating == 'poor' and score == 1:
            print('⚠️ Your password is POOR!')
            print('It is missing symbols, numbers and uppercase letters. It is 10 characters or more in length, so that is good!.')
        elif rating == 'very poor' and score == 0:
            print('❌ Your password is VERY POOR!')
            print('It is missing symbols, uppercase letters, numbers and is less than 10 characters in length.')
        elif rating == 'DANGER! HIGH RISK!!' and score == -1:
            print('🚨 Your password is VERY DANGEROUS to continue using! HIGH RISK!!')
            print('It is a VERY COMMON password AND it might be missing symbols, uppercase letters, numbers and might be less than 10 characters.')

if __name__ == '__main__':
    main()

# Homework:
# 1. Add functionality that tells the user exactly what they are missing to make their password
# stronger, such as symbols, uppercase characters, and/or more characters.
# 2. Add functionality that detects when a user adds too many sequential characters, such
# as "aaa", "111", and so on.
# 3. Check if the password contains digits as well to reach the 'secure' rating.