import re
import logging
import json

error_count = 0

most_frequent_url = None
log_counter = {}
url_counter = {}
all_logs = []

logging.basicConfig(level=logging.INFO)
with open('access.log', 'r', encoding='utf-8') as file:
    for line in file:
        m = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<HTTP_method>[A-Z]+) (?P<URL>\S+) (?P<Answer_code>\d{3})', line)
        if m:
            m = m.groupdict()
            all_logs.append(m) #Извлёк IP, HTTP-метод, URL и код ответа;
for log in all_logs:
    method = log["HTTP_method"]
    if method not in log_counter:
        log_counter[method] = 0
    log_counter[method] += 1
    error = log["Answer_code"]
    if re.match(r'4\d{2}', error):
        error_count+=1
    url = log["URL"]
    if url not in url_counter:
        url_counter[url] = 0
    url_counter[url] += 1

max_url_count = max(url_counter.values())
for key, value in url_counter.items():
    if value == max_url_count:
        most_frequent_url = key
        print(key)
#print(log_counter)
stats = {
    'requests_by_method': log_counter,
    'errors 4xx': error_count, 
    'most_frequent_url': most_frequent_url,
    'most_frequent_url_count': max_url_count
}
with open('stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, indent=3)
#print(all_logs)