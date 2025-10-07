def greet(name: str, language: str):
    if language == "it":
        print(f"Ciao, {name}!")
    elif language == "es":
        print(f"Hola, {name}!")
    else:
        print(f"Hi, {name}!")

greet("Anandakeshava", "it")
greet("ShivaTandavaBhairava", "es")
greet("Bob", "nonexistLang")

def searchUser(username: str, db: dict[str, int]) -> int | None:
    print(f"Searching for user: {username}")
    if username in db.keys():
        print(f'{username} found!')
    else:
        print(f'{username} not found...')

    return db.get(username) # IMP!! Returns None if not found. If found, returns the value.

db: dict[str, int] = {
    "Anandakeshava": 42,
    "ShivaTandavaBhairava": 7,
    "Bob": 13
}

print(searchUser("Anandakeshava", db))
print(searchUser("Alice", db))
print(searchUser("Bob", db))
print(searchUser("mariamma joseph alexandar sebastian", db))
