from parse_input import parse_input
from add_contact import add_contact
from show_all import show_all
from show_phone import show_phone
from change_contact import change_contact
from commands import all_commands, exit_commands


def main():
  contacts = {'val': '123', 'jane': '321'}
  print('Welcome to assistance bot!')

  while True:
    user_input = input('Enter a command: ')
    command, *args = parse_input(user_input)

    match command:
      case _ if command in exit_commands:
        print('Good bye!')
        break
      case 'hello':
        print('How can I help you?')
      case 'add':
        print(add_contact(args, contacts))
      case 'all':
        [print(show_all(key, value)) for key, value in contacts.items()]
      case 'phone':
        print(show_phone(args, contacts))
      case 'change':
        print(change_contact(args, contacts))
      case _:
        print(f'Invalid command. Here is the list of available commands: {
              all_commands}')


if __name__ == '__main__':
  main()
