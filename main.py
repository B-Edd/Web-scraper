import requests
from bs4 import BeautifulSoup
import re

l = []

url = "https://en.wikipedia.org/wiki/Communication"  # Replace with the desired website URL
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
text_content = soup.get_text()

# Extract words from the text content
words = re.findall(r'\b\w+\b', text_content)

# Print each word
for word in words:
    l.append(word)

for i in l:
  print(i + " ")