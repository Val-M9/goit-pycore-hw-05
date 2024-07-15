import sys
from pathlib import Path
from load_logs import load_logs
from parse_log_line import parse_log_line
from count_logs_by_level import count_logs_by_level
from display_log_count import display_log_count
from filter_logs_by_level import filter_logs_by_level


def main():
  if len(sys.argv) < 2:
    print('Enter the path to the log file as an argument')
    return

  file_path = Path(sys.argv[1])
  logs = load_logs(file_path, parse_log_line)
  if not logs:
    print('No logs to display')
    return
  logs_by_level = count_logs_by_level(logs)
  display_log_count(logs_by_level)

  if sys.argv[2:]:
    filter_level = sys.argv[2].upper()
    filtered_logs = filter_logs_by_level(logs, filter_level)

    print(f'"{filter_level}" level log details:')
    for log in filtered_logs:
      log_details = f"{log['date']} {log['time']} - {log['message']}"
      print(log_details)


if __name__ == '__main__':
  main()
