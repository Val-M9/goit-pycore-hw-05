def show_all(name: str, phone: str) -> str:
  if name:
    return f'{name}: {phone}'
  else:
    return 'There are no contacts.'
