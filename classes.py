class Address:
    def __init__(self, country, zip_code, city, street, street_number):
        self.country = country
        self.zip_code = zip_code
        self.city = city
        self.street = street
        self.street_number = street_number

    def __str__(self):
        return f"{self.street} {self.street_number}, {self.zip_code} {self.city}, {self.country}"


class Person:
    def __init__(self, name, firstname, email, phone, iban, address):
        self.name = name
        self.firstname = firstname
        self.email = email
        self.phone = phone
        self.iban = iban
        self.address = address

    def __str__(self):
        return f"{self.firstname} {self.name}\nE-Mail: {self.email}\nPhone: {self.phone}\nIBAN: {self.iban}\nAddress: {self.address}"


class User:
    def __init__(self, username, password, person):
        self.username = username
        self.password = password  # In der Realität sollte das Passwort nicht im Klartext gespeichert werden!
        self.person = person

    def __str__(self):
        return f"Username: {self.username}\n{self.person}"