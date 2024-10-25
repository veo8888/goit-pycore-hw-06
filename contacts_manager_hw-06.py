from collections import UserDict

class Field:
    """
    Базовий клас для поля запису.
    
    Атрибути:
    value (str): Значення поля.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Клас для зберігання імені контакту.
    
    Атрибути:
    value (str): Ім'я контакту.
    """
    pass

class Phone(Field):
    """
    Клас для зберігання номера телефону.
    
    Атрибути:
    value (str): Номер телефону.
    """
    def __init__(self, value):
        if self.validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Номер телефону має містити рівно 10 цифр.")

    @staticmethod
    def validate_phone(value):
        """
        Перевірка, чи є номер телефону з 10 цифр.
        
        Параметри:
        value (str): Номер телефону для перевірки.
        
        Повертає:
        bool: True, якщо номер валідний, інакше False.
        """
        return value.isdigit() and len(value) == 10

class Record:
    """
    Клас для зберігання інформації про контакт.
    
    Атрибути:
    name (Name): Ім'я контакту.
    phones (list): Список телефонів контакту.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """
        Додає номер телефону до запису.
        
        Параметри:
        phone_number (str): Номер телефону.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """
        Видаляє номер телефону зі списку.
        
        Параметри:
        phone_number (str): Номер телефону для видалення.
        """
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_number, new_number):
        """
        Замінює старий номер на новий.
        
        Параметри:
        old_number (str): Старий номер телефону.
        new_number (str): Новий номер телефону.
        """
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number

    def find_phone(self, phone_number):
        """
        Повертає телефон за номером або None, якщо не знайдено.
        
        Параметри:
        phone_number (str): Номер для пошуку.
        
        Повертає:
        Phone: Знайдений номер телефону або None.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Клас для управління адресною книгою.
    
    Атрибути:
    data (dict): Словник записів, де ключ - ім'я контакту.
    """
    def add_record(self, record):
        """
        Додає запис у книгу.
        
        Параметри:
        record (Record): Запис для додавання.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Знаходить запис за ім'ям.
        
        Параметри:
        name (str): Ім'я для пошуку.
        
        Повертає:
        Record: Знайдений запис або None.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Видаляє запис за ім'ям.
        
        Параметри:
        name (str): Ім'я контакту для видалення.
        """
        if name in self.data:
            del self.data[name]
