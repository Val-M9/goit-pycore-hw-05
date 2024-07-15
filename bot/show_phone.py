from colorama import Fore


def input_error(func):
  def wrapper(*args, **kwargs):
    try:
      if len(args[0]) > 1:
        raise IndexError
      return func(*args, **kwargs)
    except IndexError:
      return f'Please provide one value:{Fore.YELLOW} name{Fore.RESET}'
    except KeyError:
      return f'There is no contact named {Fore.YELLOW}{"".join(args[0])}{Fore.RESET}'
  return wrapper


@input_error
def show_phone(args: list[str], contacts: dict) -> str:
  return contacts[args[0]]
