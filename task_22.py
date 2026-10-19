import re
text = 'Полезные сайты: https://python.org, http://example.com/page, https://example.com/docs/index.html и ftp://files.example.com/data.'
list_of_links = re.findall(r'https?://[^\s,]+', text)
for link in list_of_links:
    print(link)