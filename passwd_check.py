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


    def check_repeats(self, password: str) -> bool:
        for c in string.ascii_letters + string.digits + string.punctuation:
            if c * 3 in password:
                return True
            
        return False


    def rate(self, password: str) -> tuple[str, bool, bool, bool, bool, bool, bool]:
    # This method returns a tuple of (rating, bool, bool, bool, bool, bool, bool)
    # rating is a string. It can be 'secure', 'medium', 'poor', 'very poor', or 'DANGER! HIGH RISK!!'
    # In order, the 6 booleans are flags that indicate: 0. very common password 1. length >= 10, 2. has uppercase, 3. has numbers (i.e. digits), 4. has punctuation AND 5. has repeats of 3 or more same characters in a row

        is_common_password_flag: bool = False
        is_length_flag: bool = False
        has_uppercase_flag: bool = False
        has_numbers_flag: bool = False
        has_punctuation_flag: bool = False
        has_repeats_flag: bool = False

        if self.is_common(password):
            is_common_password_flag = True
            return 'DANGER! HIGH RISK!!', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag

        # Calculate score
        score: int = 0

        if len(password) >= 10:  # Checks length
            is_length_flag = True
            score += 1
        if any(c.isupper() for c in password):  # Checks for uppercase characters
            has_uppercase_flag = True
            score += 1
        if any(c.isdigit() for c in password): # Checks for numbers
            has_numbers_flag = True
            score += 1
        if any(c in string.punctuation for c in password):  # Checks for punctuation
            has_punctuation_flag = True
            score += 1

        has_repeats_flag = self.check_repeats(password)

        # Return rating and score
        if score == 4:
            return 'very secure', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag
        elif score == 3:
            return 'secure', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag
        elif score == 2:
            return 'medium', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag
        elif score == 1:
            return 'poor', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag
        elif score == 0:
            return 'very poor', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag
        else:
            return 'Unknown ERROR in evaluating the password!!', is_common_password_flag, is_length_flag, has_uppercase_flag, has_numbers_flag, has_punctuation_flag, has_repeats_flag


def print_password_check_msgs(base_msg: str, length_flag: bool, uppercase_flag: bool, numbers_flag: bool, punctuation_flag: bool, repeats_flag: bool) -> None:
    print(base_msg)
    if not length_flag:
        print('However, it is missing length of 10 or more characters.')
    if not uppercase_flag:
        print('It is missing uppercase letters.')
    if not numbers_flag:
        print('It is missing numbers i.e., digits.')
    if not punctuation_flag:
        print('It is missing symbols/punctuation.')
    if repeats_flag:
        print('Improvement idea: Your password has characters that repeat 3 or more times sequentially. Consider changing that.')


# 2. Check for password
def main() -> None:
    # Link: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        rating, common_flag, length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag = validator.rate(password)
        if rating == 'very secure' and common_flag == False:
            print_password_check_msgs('✅ Your password is very secure! Your passwd IS NOT COMMON.', length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag)
        elif rating == 'secure' and common_flag == False:
            print_password_check_msgs('✅ Your password is secure! Your passwd IS NOT COMMON.', length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag)
        elif rating == 'medium' and common_flag == False:
            print_password_check_msgs('⚠️ Your password is of medium strength. It IS NOT COMMON.', length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag)
        elif rating == 'poor' and common_flag == False:
            print_password_check_msgs('⚠️ Your password is POOR! It is NOT COMMON.', length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag)
        elif rating == 'very poor' and common_flag == False:
            print_password_check_msgs('❌ Your password is VERY POOR! It is NOT COMMON.', length_flag, uppercase_flag, numbers_flag, punctuation_flag, repeats_flag)
        elif rating == 'DANGER! HIGH RISK!!':
            print('🚨 Your password is VERY DANGEROUS to continue using! HIGH RISK!!')
            print('It is a VERY COMMON password AND it might be missing symbols, uppercase letters, numbers and might be less than 10 characters.')
        elif rating == 'Unknown ERROR in evaluating the password!!':
            print('❌ An unknown error occurred while evaluating your password. Please try again.')
        else:
            print('❌ An unexpected condition occurred. Please try again.')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add functionality that tells the user exactly what they are missing to make their password
# stronger, such as symbols, uppercase characters, and/or more characters.
# 2. Add functionality that detects when a user adds too many sequential characters, such
# as "aaa", "111", and so on.
# 3. Check if the password contains digits as well to reach the 'secure' rating.
# NAILED IT!! --AP-- Oct 21, 2025