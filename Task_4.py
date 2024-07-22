# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."
    return inner

# Функція для додавання нового контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return "Contact updated."

# Функція для отримання номера телефону за ім'ям
@input_error
def phone_contact(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"The phone number for {name} is {contacts[name]}."

# Функція для показу всіх збережених контактів
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Основна функція, яка керує роботою бота
def main():
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").lower().strip()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            args = user_input.split()[1:]
            print(add_contact(args, contacts))
        elif user_input.startswith("change "):
            args = user_input.split()[1:]
            print(change_contact(args, contacts))
        elif user_input.startswith("phone "):
            args = user_input.split()[1:]
            print(phone_contact(args, contacts))
        elif user_input == "show all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# Запуск програми
if __name__ == "__main__":
    main()