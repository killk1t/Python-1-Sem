import re
import json
logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]
processed_logs = []
for log in logs:
    m = re.fullmatch(r'(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|INFO|WARNING) User (?P<user_id>\d{3}) (?P<message>.+)', log)
    if m is None:
        print('Не удалось обработать лог')
        continue
    m = m.groupdict()
    processed_logs.append(m)
for log in processed_logs:
    print(json.dumps(log, indent = 3))
