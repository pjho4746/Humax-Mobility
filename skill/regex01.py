import re

word = re.compile('[a-z]+')

# match, search, find

print(word.match('Apple'))
print(word.search('Apple'))
print(word.match('Where is My Apple'))
print(word.findall('Where is My Apple'))
