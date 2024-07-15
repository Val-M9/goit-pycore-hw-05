from typing import Callable


def load_logs(logs_path: str, parser: Callable[[str], dict]) -> list[dict]:
  try:
    with open(logs_path, 'r', encoding='utf-8') as reader:
      result = []
      line_number = 0
      while True:
        line_number += 1
        line = reader.readline()
        if not line:  # break if it is the end of the file
          break

        line = line.strip()
        if not line:  # ensure not to parse empty lines if there would be such
          continue

        try:
          parsed_line = parser(line)
          result.append(parsed_line)
        except ValueError as e:
          print(f'Error parsing line {line_number}: {line} {e}')
          continue
    return result

  except FileNotFoundError as e:
    return f'Sorry, file you are looking for was not found! {e}'
  except Exception as e:
    return f'Sorry, an error ocurred! {e}'
