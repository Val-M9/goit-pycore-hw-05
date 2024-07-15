from colorama import Fore


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except ValueError:
      return f'Please provide two values: {Fore.YELLOW}name and phone number{Fore.RESET}'

  return wrapper


@input_error
def add_contact(args: list[str], contacts: dict) -> str:
  name, phone = args
  if not contacts.get(name):
    contacts[name] = phone
    return f'{Fore.GREEN}Contact added!{Fore.RESET}'
  else:
    return f'Contact with this name already exists. If you want to update it, please, use {Fore.YELLOW}"change"{Fore.RESET} command.'
