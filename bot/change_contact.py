from colorama import Fore


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return f'Please provide two values: {Fore.YELLOW}name and phone number{Fore.RESET}'

  return wrapper


@input_error
def change_contact(args: list[str], contacts: dict) -> str:
  print(args)
  name, phone = args
  old_phone = contacts.get(name)
  if old_phone:
    contacts[name] = phone
    return f'{Fore.GREEN}Contact updated{Fore.RESET}'
  else:
    return f'{Fore.YELLOW}There is no contact with provided name{Fore.RESET}'
