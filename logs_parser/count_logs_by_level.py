from collections import Counter


def count_logs_by_level(logs: list[dict]) -> dict:
  levels = [log['level'] for log in logs]
  count = Counter(levels)
  return dict(count)
