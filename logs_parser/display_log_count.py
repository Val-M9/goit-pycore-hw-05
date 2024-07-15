def display_log_count(counts: dict) -> None:
  headers = ['Log level', 'Counter']

  header_row = ' | '.join(f'{header}' for header in headers)
  separator = '-' * len(header_row)
  column_length = [len(header) for header in headers]

  print(header_row)
  print(separator)
  for key, value in counts.items():
    print(f'{key:<{column_length[0]}} | {value:<{column_length[1]}}')
