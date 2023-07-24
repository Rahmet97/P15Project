import re

pattern = '^[+]998[0-9]{9}$'
test_string = '+998999682505'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")