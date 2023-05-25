import requests
from bs4 import BeautifulSoup

appende = []
splited = []

url = "https://en.wikipedia.org/wiki/Communication"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

words = html_content.split()


for word in words:
  splited.append(word)
print(splited)