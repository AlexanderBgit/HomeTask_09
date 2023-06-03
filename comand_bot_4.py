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

def add_contact_command():
    input_args = input('Give me name and phone with a space please: ').split()
    if len(input_args) != 2:
        print('Incorrect input. Give me name and phone with a space please.')
        return
    name, phone_number = input_args
    add_contact(name, phone_number)

def change_phone_number_command():
    input_args = input('Give me name and New phone with a space please: ').split()
    if len(input_args) != 2:
        print('Incorrect input. Give me name and New phone with a space please.')
        return
    name, new_phone_number = input_args
    change_phone_number(name, new_phone_number)

def phone_command():
    name = input('Enter user name: ')
    get_phone_number(name)

def show_all_command():
    show_all_contacts()

def process_command(command):
    command_functions = {
        'hello': lambda: print('How can I help you?'),
        'add': add_contact_command,
        'change': change_phone_number_command,
        'phone': phone_command,
        'show all': show_all_command,
        'good bye': lambda: print('Good bye!'),
        'close': lambda: print('Good bye!'),
        'exit': lambda: print('Good bye!'),
        'end': lambda: print('Good bye!')
    }

    command_function = command_functions.get(command)
    if command_function:
        command_function()
        if command in ['good bye', 'close', 'exit', 'end']:
            return False
        return True

    print('Unknown command. Try one of the following commands:')
    print('1 - hello')
    print('2 - add Give me name and phone with a space')
    print('3 - change Give me name and New phone with a space')
    print('4 - phone Enter user name')
    print('5 - show all')
    print('6 - good bye, close, exit, end')
    return True


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

        if not process_command(command):
            break

if __name__ == '__main__':
    main()
