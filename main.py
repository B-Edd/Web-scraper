import requests
from bs4 import BeautifulSoup

l = []

url = "https://en.wikipedia.org/wiki/Communication"  # Replace with the desired website URL
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
paragraphs = soup.find_all("p")  # Find all <p> elements

for paragraph in paragraphs:
    # Filter out paragraphs containing author names or other metadata
    if "author" not in paragraph.get_text().lower() and "metadata" not in paragraph.get_text().lower():
        text = paragraph.get_text(separator=" ")
        print(text)
        l.append(text)
print(l)