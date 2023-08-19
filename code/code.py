class Field:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.validate()

    def validate(self):
        pass

class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def validate(self):
        pass

class Birthday(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def validate(self):
        pass

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        pass

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if isinstance(value, Phone):
            self._phone = value
        else:
            raise ValueError("Phone must be an instance of Phone class")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if isinstance(value, Birthday):
            self._birthday = value
        else:
            raise ValueError("Birthday must be an instance of Birthday class")

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, page_size=10):
        for i in range(0, len(self.records), page_size):
            yield self.records[i:i+page_size]

address_book = AddressBook()

for page in address_book.iterator(10):
    for record in page:
        print(record.name)
