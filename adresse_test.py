from classes import Address, Person, User

u1 = User(
    input("Username:\n"),
    input("Password:\n"),
    Person(
        input("Name:\n"),
        input("Firstname:\n"),
        input("E-Mail:\n"),
        input("Phonenumber:\n"),
        input("IBAN:\n"),
        Address(
            input("Country:\n"),
            input("ZIP:\n"),
            input("City:\n"),
            input("Street:\n"),
            input("Streetnumber:\n"),
        ),
    ),
)
