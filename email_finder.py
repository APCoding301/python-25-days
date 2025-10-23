import re
from collections.abc import Iterator


def is_known_domain(email: str) -> bool:
    return email.__contains__('@gmail.com') or email.__contains__('@yahoo.com') or email.__contains__('@hotmail.com')


def extract_known_domains(all_emails: list[str]) -> list[str]:
    known_emails: Iterator[str] = filter(is_known_domain, all_emails)
    return list(known_emails)



def extract_emails(
    text: str, unique_only: bool = True, case_sensitive: bool = True
) -> list[str]:
    # Comprehensive email regex pattern
    email_pattern: str = (
        r'\b[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
        r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\.[A-Za-z]{2,}\b'
    )

    # Find all email addresses
    emails: list[str] = re.findall(email_pattern, text)

    if not case_sensitive:
        emails = [email.lower() for email in emails]

    if unique_only:
        # Remove duplicates while preserving order
        emails = list(dict.fromkeys(emails))

    return emails


def list_emails(path: str) -> None:
    emails: list[str] = []
    well_known_emails: list[str] = []

    # Also show that this works with website source code
    with open(path, 'r') as f:
        text: str = f.read()
        emails = extract_emails(text, True, False)
        well_known_emails = extract_known_domains(emails)

    if emails:
        print('All Email IDs found are:')
        for email in emails:
            print(email)
    else:
        print('No emails found...')
    
    print('-' * 40)

    if well_known_emails:
        print('Well-known domain Email IDs found are:')
        for email in well_known_emails:
            print(email)
    else:
        print('No well-known domain emails found...')
    
    print('-' * 40)


def main() -> None:
    list_emails('files/file.txt')


if __name__ == '__main__':
    main()


# Homework:
# 1. Add an option that filters out all the lesser-known domains and keeps only
# the most popular ones (gmail, yahoo, etc, etc.)