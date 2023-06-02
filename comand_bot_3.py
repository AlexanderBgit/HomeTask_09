phonebook = {}

commands = {
    'hello': 1,
    'add': 2,
    'change': 3,
    'phone': 4,
    'show all': 5,
    'good bye': 6,
    'close': 6,
    'exit': 6,
    'end': 0
}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(str(e))
        except Exception:
            print('Command processing error.')
    return wrapper

@input_error
def add_contact(name, phone_number):
    phonebook[name] = phone_number
    print(f'Contact  "{name}" with phone number "{phone_number}" has been added.')

@input_error
def change_phone_number(name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
        print(f'Phone number for contact "{name}" updated.')
    else:
        print('Contact not found.')

@input_error
def get_phone_number(name):
    if name in phonebook:
        print(f'Phone number for contact "{name}": {phonebook[name]}')
    else:
        print('Contact not found.')

def show_all_contacts():
    if phonebook:
        print('Saved contacts:')
        print('-' * 45)
        print('| {:<20} | {:<20} |'.format('Name', 'Phone number'))
        print('-' * 45)
        for name, phone_number in phonebook.items():
            print('| {:<20} | {:<20} |'.format(name, phone_number))
        print('-' * 45)
    else:
        print('No contacts saved.')

def main():
    print("Hello! I'm an assistant app. How can I help?")

    while True:
        user_input = input('Enter the command: ').lower()

        if user_input in commands:
            command = user_input
        else:
            try:
                command_index = int(user_input)
                command = list(commands.keys())[list(commands.values()).index(command_index)]
            except ValueError:
                command = None

        if command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            input_args = input('Give me name and phone with a space please: ').split()
            if len(input_args) != 2:
                print('Incorrect input. Give me name and phone with a space please.')
                continue
            name, phone_number = input_args
            add_contact(name, phone_number)

        elif command == 'change':
            input_args = input('Give me name and New phone with a space please: ').split()
            if len(input_args) != 2:
                print('Incorrect input. Give me name and New phone with a space please.')
                continue
            name, new_phone_number = input_args
            change_phone_number(name, new_phone_number)

        elif command == 'phone':
            name = input('Enter user name: ')
            get_phone_number(name)

        elif command == 'show all':
            show_all_contacts()

        elif command in ['good bye', 'close', 'exit', 'end']:
            print('Good bye!')
            break

        else:
            print('Unknown  command. Try one of the following commands:')
            print('1 - hello')
            print('2 - add Give me name and phone with a space')
            print('3 - change Give me name and New phone with a space')
            print('4 - phone Enter user name')
            print('5 - show all')
            print('6 - good bye, close, exit, end')

if __name__ == '__main__':
    main()
