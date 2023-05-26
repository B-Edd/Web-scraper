import requests
from bs4 import BeautifulSoup

def webscrape(url_for_scraping):
  l = []
  splited = []
  nonums = []
  joining = " "
  
  url = url_for_scraping  # Replace with the desired website URL
  response = requests.get(url)
  html_content = response.text
  
  soup = BeautifulSoup(html_content, "html.parser")
  paragraphs = soup.find_all("p")  # Find all <p> elements
  
  for paragraph in paragraphs:
      # Filter out paragraphs containing author names or other metadata
      if "author" not in paragraph.get_text().lower() and "metadata" not in paragraph.get_text().lower():
          text = paragraph.get_text(separator=" ")
          l.append(text)
  
  for words in l:
      words_list = words.split()
      splited.append(words_list)
  
  for words_list in splited:
    for word in words_list:
      nonums.append(word)
      #if word.isdigit():
      #  pass
      #elif word == "[" or word == "]":
       # pass
      #elif word == "-" or word == "—" or word == ".":
        #nonums.append(word)
      #elif word.isalpha():
       # nonums.append(word)

      
  joined = joining.join(nonums)
  print(joined)

ask = input("Which url?: ")
print("\n" * 3)
webscrape(ask)