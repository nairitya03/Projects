import re

text = "hello, email is talenairitya@gmail.com hello@gu.com bull@bull.com"

pattern = re.compile("[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

email = pattern.findall(text)

print(email)
