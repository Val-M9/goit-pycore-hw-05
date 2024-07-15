def parse_log_line(line: str) -> dict:
  if line:
    date, time, level, *message = line.split(' ')
    return {'date': date, 'time': time, 'level': level, 'message': ' '.join(message)}
