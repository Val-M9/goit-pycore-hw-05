def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
  filtered_logs = list(filter(lambda log: log['level'] == level, logs))

  return filtered_logs
